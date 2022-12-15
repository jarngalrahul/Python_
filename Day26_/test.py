# List Comprehension
#####################################################
#####################################################

# name = "Rahul"
# letter_list = [letter for letter in name]
# print(letter_list)

# range_list = [x*2 for x in range(1, 5)]
# print(range_list)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)

# even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)
import random
import pandas
with open("Day26_/file1.txt") as file1:
    data1 = file1.read().split('\n')
    print(data1)

with open("Day26_/file2.txt") as file2:
    data2 = file2.read().split('\n')
    print(data2)

result = [int(n) for n in data1 if n in data2 and n != '']
print(result)


# Dictionary comrehension
##################################################
##################################################
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,values) in dict.items()}

names = ['ALex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {name: score for (
    name, score) in student_scores.items() if score > 40}
print(passed_students)

# Make a dictionary which contains words as key and their length as value from the given string
sentence = "What is the airspeed velocity of an Unladen Swallow?"
resulting_dict = {word: len(word) for word in sentence.split(' ')}
print(resulting_dict)

weather_c = {
    'Monday': 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    'Sunday': 24
}

weather_f = {day: temp*9/5+32 for (day, temp) in weather_c.items()}
print(weather_f)


#Pandas and list and dictionaries
###################################################
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    print(key)
    print(value)


student_data_frame = pandas.DataFrame(student_dict)
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    print(index)
    print(row)
    # Access row.student or row.score
    print(f"Name of the student:{row.student}, Score:{row['score']}")
