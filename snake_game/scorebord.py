from turtle import Turtle


class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.show()

    def add(self):
        self.clear()
        self.score += 1
        self.show()

    def show(self):
        self.color('yellow')
        self.penup()
        self.goto(0, 280)
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=('Arial', 12, 'normal'))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game over", move=False, align='center', font=('Arial', 10, 'normal'))





