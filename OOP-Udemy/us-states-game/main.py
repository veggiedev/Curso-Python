from turtle import Turtle, Screen
import pandas as pd
import csv
data = pd.read_csv('OOP-Udemy/us-states-game/50_states.csv')    
screen = Screen()
screen.setup(750, 600)
screen.bgpic('OOP-Udemy/us-states-game/blank_states_img.gif')
state_turtle = Turtle()
state_turtle.hideturtle()
state_turtle.color('black')
state_turtle.penup()     
all_state_data = data.state.to_list()
print(all_state_data)
guesses = []
not_guessed = []
game_on = True
for entry in all_state_data:
    not_guessed.append(entry)
while game_on == True:
    guess = screen.textinput(f'Guess a State. {len(guesses)}/50', 'What state do you want to guess?').title()
    if guess == 'Exit':
        break
    elif guess in all_state_data:
        not_guessed.remove(guess)
        not_guessed_dict = {'States': not_guessed}
        state_data = data[data.state == guess]
        state_turtle.goto(int(state_data.x), int(state_data.y))
        state_turtle.write(guess, font=('Courier', 16))
        guesses.append(guess)
print(not_guessed) 
df = pd.DataFrame(not_guessed_dict)
df.to_csv('OOP-Udemy/us-states-game/states_to_learn.csv') 

    

















screen.exitonclick()