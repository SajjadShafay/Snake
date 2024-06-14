from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as file:
            self.highscore = int(file.read())
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
