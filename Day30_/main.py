# Errors and Exceptions
import pandas
# Reading the csv file using pandas
data = pandas.read_csv("Day30_//nato_phonetic_alphabet.csv")
# Making a dictionary of letter and codes
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def convert_to_phontic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[char] for char in word]
    except KeyError:
        print("Sorry only letters in alphabet please")
        convert_to_phontic()
    else:
        print(output_list)


convert_to_phontic()
