from turtle import Turtle, Screen
import pandas as pd
import csv

screen = Screen()
screen.setup(750, 600)
screen.bgpic('OOP-Udemy/us-states-game/blank_states_img.gif')    
data = pd.read_csv('OOP-Udemy/us-states-game/50_states.csv')    
all_state_data = data.state.to_list()
guesses = []
all_states_list = []  
game_is_on = True
state_turtle = Turtle()
state_turtle.hideturtle()
state_turtle.color('black')
state_turtle.penup() 
while game_is_on:
    not_guessed = []  
    guess = screen.textinput(f'Guess a State. {len(guesses)}/50', 'What state do you want to guess?').title()
    rows = []
    fields = []
    with open('OOP-Udemy/us-states-game/50_states.csv') as file:
        states = csv.reader(file)
        fields = next(states)
        for state in states:   
            if guess == 'Exit':
                # for item in states:
                if state not in guesses:
                    not_guessed.append(state[0].split(','))
                with open('OOP-Udemy/us-states-game/states_to_learn.csv', 'w') as file:
                    csvwriter = csv.writer(file) 
                    csvwriter.writerows(not_guessed)
                game_is_on = False         
            elif guess in state:
                guesses.append(guess)
                guess_x = int(state[1])
                guess_y = int(state[2])
                state_turtle.goto(guess_x, guess_y)
                state_turtle.write(guess, font=('Courier', 15))
            


            
       
       
       
       
       
       
       
       
       
       
       
       
       
        # for row in states:
        #     for item in all_states_list:
        #         if item in guesses:
        #             all_states_list.remove(item) 
        #     with open('OOP-Udemy/us-states-game/states_to_learn.csv', 'w') as file:
        #         csvwriter = csv.writer(file) 
        #         csvwriter.writerows(all_states_list)
        # for state in states:
        #     all_states_list.append(state[0].split(','))
        # if len(guesses) == 50 or guess == 'Exit':
        #     game_is_on = False   
            
        #     print(all_states_list)
        #     # for row in states:
            #     if guess == 50 or guess == 'Exit':
            #         # for row in states:
            #             print(row)

            #             if row not in guesses:
            #                 not_guessed.append(row[0].split(','))
            #                 print(not_guessed)

            #             print(guesses)
            #             game_is_on = False
                    
        # else:
        #     if guess in row:
        #         guesses.append(guess)
        #         guess_x = int(row[1])
        #         guess_y = int(row[2])
        #         state_turtle.goto(guess_x, guess_y)
        #         state_turtle.write(guess, font=('Courier', 15))
screen.exitonclick()