from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10
        self.move_speed = 0.1
        
    
    
    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x,new_y)
    
    def ceiling_floor_collision(self):
        self.y_direction *= -1
        
    def r_paddle_bounce(self):
        self.x_direction = -(abs(self.x_direction))
        self.move_speed *= 0.9
    
    def l_paddle_bounce(self):
        self.x_direction = (abs(self.x_direction))
        self.move_speed *= 0.9
        
        
    def out(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_direction *= -1
    
            