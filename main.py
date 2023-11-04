
with open("./Input/Names/invited_names.txt") as names_file:   #opening names
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    print(letter_content)


