from turtle import Turtle

class Paddle(Turtle):

    # creating paddle
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    # creating paddle movement
    def paddle_movement_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_movement_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


