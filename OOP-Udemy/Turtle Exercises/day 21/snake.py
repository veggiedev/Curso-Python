from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)        
        self.segments[0].forward(MOVING_DISTANCE)
    
    def heading(self):
        return self.segments[0].heading()
    
    def setheading(self, heading_coord):
        for seg in self.segments:
            seg.setheading(heading_coord)
            
    def xcor(self):
        return self.segments[0].xcor()
    def ycor(self):
        return self.segments[0].ycor()
    
    def grow(self):
        for self.segment in range(1):
            new_segment = Turtle("square")
            new_segment.hideturtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.turtlesize(1)            
            self.segments.append(new_segment)
            new_segment.showturtle()

    
    def stop(self):       
        self.segments[0].forward(0)
        
