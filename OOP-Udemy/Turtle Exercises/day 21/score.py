from turtle import Turtle, Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 270)
        
    def get_score(self, score):
        self.write(f"SCORE: {score}",  move=True, align="center", font=("Arial", 20, "normal"))
            
        
    #     self.decimal = (8, 270)
    #     self.non_decimal = (22, 270)
    #     self.score_turtle = Turtle()
    # # def drawing(self):       
    #     # self.turtle_one = Turtle()
    #     # self.turtle_two = Turtle()
    #     # self.turtle_three = Turtle()
    #     # self.turtle_four = Turtle() 
    #     # self.turtle_five = Turtle()
    #     # self.turtle_six = Turtle()
    #     # self.turtle_seven = Turtle()
    #     # self.turtle_eight = Turtle()
    #     # self.turtle_nine = Turtle()
    #     # self.turtle_zero = Turtle()

    # def score_drawing(self):
    #     self.score_turtle.setheading(0)
    #     self.score_turtle.hideturtle()
    #     self.score_turtle.penup()
    #     self.score_turtle.pensize(3)
    #     self.score_turtle.color("white")
    #     self.score_turtle.goto(-55, 270)
    #     self.score_turtle.pendown()
    #     # "S"
    #     self.score_turtle.back(10)
    #     self.score_turtle.right(90)
    #     self.score_turtle.forward(5)
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(10)
    #     self.score_turtle.right(90)
    #     self.score_turtle.forward(5)
    #     self.score_turtle.right(90)
    #     self.score_turtle.forward(10)
    #     self.score_turtle.penup()
    #     self.score_turtle.setheading(0)
    #     self.score_turtle.forward(15)
    #     # "C"
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(10)
    #     self.score_turtle.right(90)
    #     self.score_turtle.pendown()
    #     self.score_turtle.forward(8)
    #     self.score_turtle.back(8)
    #     self.score_turtle.right(90)
    #     self.score_turtle.forward(10)
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(8)
    #     self.score_turtle.penup()
    #     self.score_turtle.forward(5)
    #     # "O"
    #     self.score_turtle.pendown()
    #     self.score_turtle.forward(8)
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(10)
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(8)
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(10)
    #     self.score_turtle.setheading(0)
    #     self.score_turtle.penup()
    #     self.score_turtle.forward(15)
    #     self.score_turtle.pendown()
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(5)
    #     self.score_turtle.right(90)
    #     self.score_turtle.forward(6)
    #     self.score_turtle.right(60)
    #     self.score_turtle.forward(6)
    #     self.score_turtle.back(6)
    #     self.score_turtle.setheading(90)
    #     self.score_turtle.forward(5)
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(6)
    #     self.score_turtle.setheading(0)
    #     self.score_turtle.penup()
    #     self.score_turtle.forward(14)
    #     self.score_turtle.pendown()
    #     self.score_turtle.forward(7)
    #     self.score_turtle.back(7)
    #     self.score_turtle.right(90)
    #     self.score_turtle.forward(5)
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(6)
    #     self.score_turtle.back(6)
    #     self.score_turtle.right(90)
    #     self.score_turtle.forward(5)
    #     self.score_turtle.left(90)
    #     self.score_turtle.forward(7)
        
    # def number_one(self, coords_score):
    #     self.turtle_one.setheading(0)
    #     self.turtle_one.hideturtle()
    #     self.turtle_one.penup()
    #     self.turtle_one.pensize(3)
    #     self.turtle_one.color("white")
    #     self.turtle_one.goto(coords_score)
    #     self.turtle_one.pendown()
    #     self.turtle_one.right(90)
    #     self.turtle_one.forward(10)
    #     self.turtle_one.penup()
    #     self.turtle_one.goto(coords_score)   

    # def number_two(self, coords_score):
    #     self.turtle_two.setheading(0)
    #     self.turtle_two.hideturtle()
    #     self.turtle_two.penup()
    #     self.turtle_two.pensize(3)
    #     self.turtle_two.color("white")
    #     self.turtle_two.goto(coords_score)
    #     self.turtle_two.pendown()
    #     self.turtle_two.forward(10)
    #     self.turtle_two.right(90)
    #     self.turtle_two.forward(5)
    #     self.turtle_two.right(90)
    #     self.turtle_two.forward(10)
    #     self.turtle_two.left(90)
    #     self.turtle_two.forward(5)
    #     self.turtle_two.left(90)
    #     self.turtle_two.forward(10)
    #     self.turtle_two.penup()
    #     self.turtle_two.goto(coords_score)         

    # def number_three(self, coords_score):
    #     self.turtle_three.setheading(0)
    #     self.turtle_three.hideturtle()
    #     self.turtle_three.penup()
    #     self.turtle_three.pensize(3)
    #     self.turtle_three.color("white")
    #     self.turtle_three.goto(coords_score)
    #     self.turtle_three.pendown()
    #     self.turtle_three.forward(10)
    #     self.turtle_three.right(90)
    #     self.turtle_three.forward(5)
    #     self.turtle_three.right(90)
    #     self.turtle_three.forward(5)
    #     self.turtle_three.back(5)
    #     self.turtle_three.left(90)
    #     self.turtle_three.forward(5)
    #     self.turtle_three.left(90)
    #     self.turtle_three.back(10)
    #     self.turtle_three.penup()    
    #     self.turtle_three.goto(coords_score)    
        
    # def number_four(self, coords_score):
    #     self.turtle_four.setheading(0)
    #     self.turtle_four.hideturtle()
    #     self.turtle_four.penup()
    #     self.turtle_four.pensize(3)
    #     self.turtle_four.color("white")
    #     self.turtle_four.goto(coords_score)
    #     self.turtle_four.pendown()
    #     self.turtle_four.right(90)
    #     self.turtle_four.forward(5)
    #     self.turtle_four.left(90)
    #     self.turtle_four.forward(5)
    #     self.turtle_four.left(90)
    #     self.turtle_four.forward(5)
    #     self.turtle_four.back(10)
    #     self.turtle_four.penup()
    #     self.turtle_four.goto(coords_score)  
    
    # def number_five(self, coords_score):
    #     self.turtle_five.setheading(0)
    #     self.turtle_five.hideturtle()
    #     self.turtle_five.penup()
    #     self.turtle_five.pensize(3)
    #     self.turtle_five.color("white")
    #     self.turtle_five.goto(coords_score)
    #     self.turtle_five.pendown()
    #     self.turtle_five.forward(5)
    #     self.turtle_five.back(5)
    #     self.turtle_five.right(90)
    #     self.turtle_five.forward(5)
    #     self.turtle_five.left(90)
    #     self.turtle_five.forward(5)
    #     self.turtle_five.right(90)
    #     self.turtle_five.forward(5)
    #     self.turtle_five.right(90)
    #     self.turtle_five.forward(5)
    #     self.turtle_five.penup()
    #     self.turtle_five.goto(coords_score) 
        
    # def number_six(self, coords_score):
    #     self.turtle_six.setheading(0)
    #     self.turtle_six.hideturtle()
    #     self.turtle_six.penup()
    #     self.turtle_six.pensize(3)
    #     self.turtle_six.color("white")
    #     self.turtle_six.goto(coords_score)
    #     self.turtle_six.pendown()
    #     self.turtle_six.forward(5)
    #     self.turtle_six.back(5)
    #     self.turtle_six.right(90)
    #     self.turtle_six.forward(5)
    #     self.turtle_six.left(90)
    #     self.turtle_six.forward(5)
    #     self.turtle_six.right(90)
    #     self.turtle_six.forward(5)
    #     self.turtle_six.right(90)
    #     self.turtle_six.forward(5)
    #     self.turtle_six.right(90)
    #     self.turtle_six.forward(5)
    #     self.turtle_six.penup()
    #     self.turtle_six.goto(coords_score)   

    # def number_seven(self, coords_score):
    #     self.turtle_seven.setheading(0)
    #     self.turtle_seven.hideturtle()
    #     self.turtle_seven.penup()
    #     self.turtle_seven.pensize(3)
    #     self.turtle_seven.color("white")
    #     self.turtle_seven.goto(coords_score)
    #     self.turtle_seven.pendown()
    #     self.turtle_seven.forward(5)
    #     self.turtle_seven.right(90)
    #     self.turtle_seven.forward(10)
    #     self.turtle_seven.penup()
    #     self.turtle_seven.goto(coords_score)    

    # def number_eight(self, coords_score):
    #     self.turtle_eight.setheading(0)
    #     self.turtle_eight.hideturtle()
    #     self.turtle_eight.penup()
    #     self.turtle_eight.pensize(3)
    #     self.turtle_eight.color("white")
    #     self.turtle_eight.goto(coords_score)
    #     self.turtle_eight.pendown()
    #     self.turtle_eight.forward(5)
    #     self.turtle_eight.right(90)
    #     self.turtle_eight.forward(10)
    #     self.turtle_eight.right(90)
    #     self.turtle_eight.forward(5)
    #     self.turtle_eight.right(90)
    #     self.turtle_eight.forward(5)
    #     self.turtle_eight.right(90)
    #     self.turtle_eight.forward(5)
    #     self.turtle_eight.back(5)
    #     self.turtle_eight.left(90)
    #     self.turtle_eight.forward(5)
    #     self.turtle_eight.penup()
    #     self.turtle_eight.goto(coords_score)
        
    # def number_nine(self, coords_score):
    #     self.turtle_nine.setheading(0)
    #     self.turtle_nine.hideturtle()
    #     self.turtle_nine.penup()
    #     self.turtle_nine.pensize(3)
    #     self.turtle_nine.color("white")
    #     self.turtle_nine.goto(coords_score)
    #     self.turtle_nine.pendown()
    #     self.turtle_nine.forward(5)
    #     self.turtle_nine.right(90)
    #     self.turtle_nine.forward(10)
    #     self.turtle_nine.right(90)
    #     self.turtle_nine.forward(5)
    #     self.turtle_nine.right(90)
    #     self.turtle_nine.penup()
    #     self.turtle_nine.forward(5)
    #     self.turtle_nine.pendown()
    #     self.turtle_nine.right(90)
    #     self.turtle_nine.forward(5)
    #     self.turtle_nine.back(5)
    #     self.turtle_nine.left(90)
    #     self.turtle_nine.forward(5)
    #     self.turtle_nine.penup()
    #     self.turtle_nine.goto(coords_score)
            
    # def number_zero(self, coords_score):
    #     self.turtle_zero.setheading(0)
    #     self.turtle_zero.hideturtle()
    #     self.turtle_zero.penup()
    #     self.turtle_zero.pensize(3)
    #     self.turtle_zero.color("white")
    #     self.turtle_zero.goto(coords_score)
    #     self.turtle_zero.pendown()
    #     self.turtle_zero.forward(5)
    #     self.turtle_zero.right(90)
    #     self.turtle_zero.forward(10)
    #     self.turtle_zero.right(90)
    #     self.turtle_zero.forward(5)
    #     self.turtle_zero.right(90)
    #     self.turtle_zero.forward(10)
            
    # def run_scores(self, numbers, score):
        
    

    #     self.turtle_one = Turtle()
    #     self.turtle_two = Turtle()
    #     self.turtle_three = Turtle()
    #     self.turtle_four = Turtle() 
    #     self.turtle_five = Turtle()
    #     self.turtle_six = Turtle()
    #     self.turtle_seven = Turtle()
    #     self.turtle_eight = Turtle()
    #     self.turtle_nine = Turtle()
    #     self.turtle_zero = Turtle()
    #     if numbers[0] == 0: 
    #         self.number_zero(self.decimal)   
    #     elif numbers[0] == 1:
    #         self.turtle_zero.reset()
    #         self.number_one(self.decimal)
            
    #     elif numbers[0] == 2:
    #         self.turtle_one.reset()
    #         self.number_two(self.decimal)
    #     elif numbers[0] == 3:
    #         self.turtle_two.reset()
    #         self.number_three(self.decimal)
    #     elif numbers[0] == 4:
    #         self.turtle_three.reset()
    #         self.number_four(self.decimal)
    #     elif numbers[0] == 5:
    #         self.turtle_four.reset()
    #         self.number_five(self.decimal)
    #     elif numbers[0] == 6:
    #         self.turtle_five.reset()
    #         self.number_six(self.decimal)
    #     elif numbers[0] == 7:
    #         self.turtle_six.reset()
    #         self.number_seven(self.decimal)
    #     elif numbers[0] == 8:
    #         self.turtle_seven.reset()
    #         self.number_eight(self.decimal)
    #     elif numbers[0] == 9:
    #         self.turtle_eight.reset()
    #         self.number_nine(self.decimal)
    #     elif numbers[0] == 0:
    #         self.turtle_nine.reset()
    #         self.number_zero(self.decimal)
    #     if score > 9:
    #         if numbers[1] == 1:
    #             self.turtle_zero.reset()
    #             self.number_one(self.non_decimal)
    #         elif numbers[1] == 2:
    #             self.turtle_one.reset()
    #             self.number_two(self.non_decimal)
    #         elif numbers[1] == 3:
    #             self.turtle_two.reset()
    #             self.number_three(self.non_decimal)
    #         elif numbers[1] == 4:
    #             self.turtle_three.reset()
    #             self.number_four(self.non_decimal)
    #         elif numbers[1] == 5:
    #             self.turtle_four.reset()
    #             self.number_five(self.non_decimal)
    #         elif numbers[1] == 6:
    #             self.turtle_five.reset()
    #             self.number_six(self.non_decimal)
    #         elif numbers[1] == 7:
    #             self.turtle_six.reset()
    #             self.number_seven(self.non_decimal)
    #         elif numbers[1] == 8:
    #             self.turtle_seven.reset()
    #             self.number_eight(self.non_decimal)
    #         elif numbers[1] == 9:
    #             self.turtle_eight.reset()
    #             self.number_nine(self.non_decimal)
    #         elif numbers[1] == 0:
    #             self.turtle_nine.reset()
    #             self.number_zero(self.non_decimal)    
                
                