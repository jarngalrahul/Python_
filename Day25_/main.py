import pandas
FILE_PATH = "Day25_/Central_Park_Squirrel_Census.csv"

data_list = pandas.read_csv(FILE_PATH)
grey = len(data_list[data_list['Primary Fur Color'] == "Gray"])
red = len(data_list[data_list['Primary Fur Color'] == "Cinnamon"])
black = len(data_list[data_list['Primary Fur Color'] == "Black"])
print(grey, red, black)

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Day25_/squirrel_count.csv")
