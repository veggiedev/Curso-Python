#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

letter_p = ''                
with open ('OOP-Udemy/Mail Merge Project Start/Input/Names/invited_names.txt', 'r') as names_list:
    names = names_list.readlines()

with open ('OOP-Udemy/Mail Merge Project Start/Input/Letters/starting_letter.txt', 'r+') as empty_letter:
    letter = empty_letter.readlines()
    

for sentence in letter[2:]:
    letter_p += sentence
        


for name in names:
        with open (f'OOP-Udemy/Mail Merge Project Start/Output/ReadyToSend/letter_to_{name}', 'w') as file:
            stripped_name = name.strip()
            new_letter = file.write(f'Dear {stripped_name},\n \n{letter_p}')

# for name in names:
#         with open (f'OOP-Udemy/Mail Merge Project Start/Output/ReadyToSend/letter_to_{name}', 'w') as file:
#             new_letter = file.write(f'Dear {name},You are invited to my birthday this Saturday.\nHope you can make it!\nAngel')
