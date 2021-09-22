from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        with open("HIGH_SCORE.txt", "r") as file:
            self.high_score = int(file.read())
        self.hideturtle()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("HIGH_SCORE.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)
