from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Verdana", 25, "normal")
FONT2 = ("Verdana", 20, "normal")
POSITION = (0, 255)

class Scoreboard(Turtle):
    
    def __init__(self, name1, name2):
        super().__init__()
        self.name1 = name1
        self.name2 = name2
        self.start_time = time.time()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"{self.name1}: {self.player1_score}", align=ALIGNMENT, font=FONT)#Player: score
        self.goto(150, 250)
        self.write(f"{self.name2}: {self.player2_score}", align=ALIGNMENT, font=FONT)
        self.goto(0, 230)
        self.write(f"{int(time.time() - self.start_time)}", align=ALIGNMENT, font=FONT2)#Live time - Start time

    def player1_point(self):
        self.player1_score += 1

    def player2_point(self):
        self.player2_score += 1

    def game_over(self, player):
        self.clear()
        self.goto(0, 100)
        self.write(f"GAME OVER - Winner: {player}", align=ALIGNMENT, font=FONT)
