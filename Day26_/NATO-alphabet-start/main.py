import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("Day26_/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (_, row) in df.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name? ").upper()
lst = [phonetic_dict[character] for character in user_input]
print(lst)
