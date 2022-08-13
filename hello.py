# by writing 'python' and the name of the file (that you want to run), in the terminal, the code runs itself
# by writing 'code' and the name of the file you want to create, you create a new file.
# The 'input' function let's the user input a string(a sequence of text). Name is a variable, which has the value of  what's on the other side of the equals sign. Strip and title are defined further down.
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
# Splits the string 'name' into multiple substrings, 'first' and 'last'
first, last = name.split(" ")


# Third way
print(f"Hello, {first}")
