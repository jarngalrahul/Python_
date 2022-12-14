# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# start
with open("Day24_//Mail Merge Project Start//Input//Letters//starting_letter.txt") as file:
    letter = file.read()

with open("Day24_/Mail Merge Project Start//Input//Names//invited_names.txt") as names:
    names = names.read().split('\n')
    for name in names:
        with open(f"Day24_/Mail Merge Project Start//Output//ReadyToSend//{name}_letter.txt", mode='w') as output:
            temp = letter.replace('[name]', name)
            output.write(temp)
