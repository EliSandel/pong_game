from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.turtlesize(5,1)
        self.color("white")
        self.penup()
        self.goto(self.x,self.y)
        
    def up(self):
        self.y += 20
        self.goto(self.x,self.y)

    
    def down(self):
        self.y -= 20
        self.goto(self.x,self.y)
