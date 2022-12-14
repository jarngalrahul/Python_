# READING FILE
#####################################
# Opened file needs to be closed by default it is in read only mode
# Method 1:
file = open('Day24_/File_I/my_file.txt')
contents = file.read()
print(contents)
file.close()


# Using this method we don't need to manually close the files
# Method 2:
with open('Day24_//File_I//my_file.txt') as file:
    contents = file.read()
    print(contents)


# WRITING ON FILE
#######################################
# Method 1: Overwriting on given file/ if file is not present compiler automatically creates it
with open('Day24_//File_I//my_file.txt', mode='w') as file:
    file.write("Overwritten the previous text.")

# method 2: Appending the text
with open("Day24_//File_I//my_file.txt", mode='a') as file:
    file.write('\nAppnded text')
