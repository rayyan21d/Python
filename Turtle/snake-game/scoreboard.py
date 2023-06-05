from turtle import Turtle

FONT = "ARIAL"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=(FONT, 24, "normal"))    
        
    def  increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=(FONT, 24, "normal"))    