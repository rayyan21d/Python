from turtle import Turtle
HIGH_SCORE = 0

FONT = "ARIAL"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        # High score from txt file
        with open("./data.txt") as file:
            self.high_score = int(file.read())
            
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HIGH SCORE: {self.high_score}", align="center", font=(FONT, 24, "normal"))    
        
    def  increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
                
                
        self.score = 0
        self.update_scoreboard()        