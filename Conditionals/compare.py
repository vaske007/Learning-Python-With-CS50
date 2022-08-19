x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y: # Here we asked a question is x less then y, if so print the code below. 'x < y' is called a Boolean expression, named after a mathemathician Bool. A Boolean expresion is a questions with a yes or no answer, or actually a true or false answer.
    print("x is less than y")
elif x > y: # If the if statment above isn't true, the code will check whether or not this elif program is true
    print("x is greater than y")
else: # If none of the statements above are true, the code will run this line. The upside to using else, instead of elif, is faster code, which isn't noticeable now, but if we had a much bigger and more complex code, this would help it to run faster.
    print("x is equal to")