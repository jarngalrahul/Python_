# Studying pandas and working with data files(csv - Comma seperated values).
import pandas
import csv
FILE_PATH = "Day25_//weather_data.csv"

# with open(FILE_PATH) as data:
#     weather_data = []
#     while data.readline():
#         weather_data.append(data.readline().strip())
#     print(weather_data)

###################################
# OR using csv library
###################################
# with open(FILE_PATH) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


# #####################################
# # USING PANDAS
# #####################################
# data = pandas.read_csv(FILE_PATH)
# # print(data)
# # print(data[['day', 'condition']])
# # print(data[data['condition'] == "Sunny"])

# # Average of temps
# temps = data['temp']
# print(sum(temps)/len(temps))
# # or
# print(data['temp'].mean())
# # maximum temperature
# print(data['temp'].max())

# # getting row and acessing it
# monday = data[data.day == 'Monday']
# print(monday.condition)
# print(monday.temp)


############################################
# Creating Datafram
############################################
data_list = {
    "students": ["Pam", "El'Primo", "Angela", "Rahul"],
    "scores": [76, 56, 65, 99]
}
data = pandas.DataFrame(data_list)
data.to_csv("Day25_/new__file.csv")
