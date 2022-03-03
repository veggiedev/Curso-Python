from turtle import Turtle, Screen
import random

tim = Turtle()
tom = Turtle()
ted = Turtle()
troy = Turtle()
screen = Screen()
screen.setup(1080, 720)
tim_total_distance = 0
tom_total_distance = 0
ted_total_distance = 0
troy_total_distance = 0
guess_winner = screen.textinput('Guess the winner', 'Who is gonna win? red, blue, green or yellow')
winning_turtle = ''
tim.penup()
tim.forward(400)
tim.right(90)
tim.forward(200)
tim.left(180)
tim.pendown()
tim.forward(400)
tim.penup()
tim.home()

tim.penup()
tim.backward(400)
tim.color("green")
tim.shape("turtle")

tom.penup()
tom.backward(400)
tom.color("blue")
tom.shape("turtle")
tom.right(90)
tom.forward(50)
tom.left(90)

ted.penup()
ted.backward(400)
ted.color("red")
ted.shape("turtle")
ted.left(90)
ted.forward(50)
ted.right(90)

troy.penup()
troy.backward(400)
troy.color("yellow")
troy.shape("turtle")
troy.right(90)
troy.forward(100)
troy.left(90)
no_winner = True
while no_winner == True:
    # travel = random.choice(distance)
    # for move in range(400):
    travel_tim = random.randint(1, 100)        
    tim.forward(travel_tim)
    tim_total_distance += travel_tim
    travel_tom = random.randint(1, 100)
    tom.forward(travel_tom)
    tom_total_distance += travel_tom
    travel_ted = random.randint(1, 100)
    ted.forward(travel_ted)
    ted_total_distance += travel_ted
    travel_troy = random.randint(1, 100)
    troy.forward(travel_troy)
    troy_total_distance += travel_troy
    print(tim_total_distance)
    print(tom_total_distance)  
    print(ted_total_distance)  
    print(troy_total_distance)           
    if tim_total_distance > 800:
        no_winner = False
        print('The winner is the green turtle')
        winning_turtle = 'green'
        if guess_winner == winning_turtle:
            print('You win') 
        else:
            print('You lose.')
         
    elif tom_total_distance > 800:
        no_winner = False
        print('The winner is the blue turtle')
        winning_turtle = 'blue'
        if guess_winner == winning_turtle:
            print('You win')
        else:
            print('You lose.')
    elif ted_total_distance > 800:
        no_winner = False
        print('The winner is the red turtle')
        winning_turtle = 'red'
        if guess_winner == winning_turtle:
            print('You win')
        else:
            print('You lose.')
    elif troy_total_distance > 800:
        no_winner = False
        print('The winner is the yellow turtle')
        winning_turtle = 'yellow'
        if guess_winner == winning_turtle:
            print('You win')
        else:
            print('You lose.')

screen.exitonclick()