# by writing 'python' and the name of the file (that you want to run), in the terminal, the code runs itself
# by writing 'code' and the name of the file you want to create, you create a new file.
# by writing 'python' in your terminal, you enter the interactive mode. Where all you need to do, is write a line off code and press 'enter', and the code will run. To exit the interactive mode press Ctrl-z (on windows).
# by writing 'def', which stands for define, you can create your own function. The point of making your own functions is to not have to repeat yourself. You have to define the function before calling it. You can't call the function in line 1, and define the function in line 2

def main(): # You usually put the main part of your code in this compartment. It is not necessary, but it is a convention. Though note that 'name' exists only in the scope of the main function, so you can not call it in your 'hello' function
    name = input("What's your name? ")
    hello(name)


def hello(to="world"): # What happens here, is if the parameter 'to' hasn't been given any value, the default of this parameter will be 'world'
    print("Hello,", to)

main() # Calling our function. Because we are calling our function at the end of the file, we can put the code in any order we want.