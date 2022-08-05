#by writing 'python' and the name of the file (that you want to run), in the terminal, the code runs itself
#by writing 'code' and the name of the file you want to create, you create a new file.
name = input("What's your name? ").strip().title() # The 'input' function let's the user input a string(a sequence of text). Name is a variable, which has the value of  what's on the other side of the equals sign. Strip and title are defined further down.

# Removes whitespace from the str(string), in other words, it takes away the "spaces". Title is defined in line 11
#name = name.strip().title()

# Capitalizes the user's name (makes the first letter uppercase, and the rest lowercase)
#name = name.capitalize()

# Does the same thing as name.capitalize, but instead of only making the first letter uppercase, it makes all the letters at the begging of the words uppercase 
#name = name.title()


# First way
print("Hello,", name) # The print function prints onto the screen whatever is within the parenthesis, as long as it is recongizable to the computer

# Second way
print("Hello, ", end="") # End is a parameter, there are multiple parameters in the print function
print(name)

# Third way
print(f"Hello, {name}")
