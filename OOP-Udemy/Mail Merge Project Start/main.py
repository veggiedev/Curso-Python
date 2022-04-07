letter_p = '' 
              
with open ('OOP-Udemy/Mail Merge Project Start/Input/Names/invited_names.txt', 'r') as names_list:
    names = names_list.readlines()

with open ('OOP-Udemy/Mail Merge Project Start/Input/Letters/starting_letter.txt', 'r+') as empty_letter:
    letter = empty_letter.readlines()

for sentence in letter[2:]:
    letter_p += sentence

for name in names:
        with open (f'OOP-Udemy/Mail Merge Project Start/Output/ReadyToSend/letter_to_{name}.txt', 'w') as file:
            stripped_name = name.strip()
            new_letter = file.write(f'Dear {stripped_name},\n \n{letter_p}')