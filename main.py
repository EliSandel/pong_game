from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

# initalizing paddles
player_l = Paddle(-350,0)
player_r = Paddle(350,0)
ball = Ball()
scoreboard = Scoreboard()

#up down functions
screen.listen()
screen.onkey(player_r.up, "Up")
screen.onkey(player_r.down, "Down")
screen.onkey(player_l.up, "w")
screen.onkey(player_l.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with ceiling and floor
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.ceiling_floor_collision()
        
    #Detect collision with right and left paddle
    if ball.distance(player_r) < 50 and ball.xcor() > 320 and ball.xcor() < 350:
        ball.r_paddle_bounce()
    
    if ball.distance(player_l) < 50 and ball.xcor() < -320 and ball.xcor() > -350:
        ball.l_paddle_bounce()
    
    #Detect collision with right wall
    if ball.xcor() > 360:
        ball.out()
        scoreboard.player_l_point()
        screen.update()
        time.sleep(0.5)
        
    
    #Detect collision with left wall
    if ball.xcor() < -360:
        ball.out()
        scoreboard.player_r_point()
        screen.update()
        time.sleep(0.5)
        
    



screen.exitonclick()