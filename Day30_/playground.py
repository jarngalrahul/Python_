# Exception Handling

# try - Something that might cause an exception
# catch - Do this if there is an exception
# else - If there were no exception
# finally - Carry out no matter what happens
# ---------------------------------------------------------------------#
# try:
#     file = open("doesnotexist.txt")
#     dict = {"key": "value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("doesnotexist.txt", "w")
#     file.write("something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist!!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
# ---------------------------------------------------------------------#
# height = float(input("Enter your height in (m): "))
# weight = float(input("Enter your weight in (kg): "))

# if height > 3:
#     raise ValueError("Average human height does not exceed 3mtrs")

# print(f"MBI = {weight/height**2}")
# ---------------------------Challenge------------------------------------------#
fruits = ["apple", "orange", "pears"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as msg:
        print(f"{msg}")
    else:
        print(fruit+" pie")


make_pie(int(input("Enter the index: ")))
