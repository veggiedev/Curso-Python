# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass
import pandas

alphabet_dict = pandas.read_csv('OOP-Udemy/NATO-alphabet-start/nato_phonetic_alphabet.csv').to_dict()
print(alphabet_dict)
word_list = []
word = input('Enter word, please: ').upper()

df_alphabet = pandas.DataFrame(alphabet_dict)
#Loop through rows of a data frame

    #Access index and row
    #Access row.student or row.score

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter: row.code for (index, row) in df_alphabet.iterrows()}




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

phonetic_list = [phonetic_dict[letter] for letter in word]

print(phonetic_list)

# for letter in word.upper():
#     for (index, row) in df_alphabet.iterrows():
#         if letter == row.letter:
#             word_list.append(row.code)
# print(word_list)

