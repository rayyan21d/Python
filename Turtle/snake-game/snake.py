from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")
        
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("green")
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def create_snake(self):
        
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
            
    def move(self):
  
        for segment_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_num-1].xcor()
            new_y = self.segments[segment_num-1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)   
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def detect_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
    
    
    def reset(self):
        for seg in self.segments:
            seg.goto(20000, 20000) 
        
        
        self.segments.clear()
        self.__init__()