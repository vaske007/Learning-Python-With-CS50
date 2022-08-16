# 'int', which is short for integers, is a number all the way toward negative infinity, and all the way toward positive infinity. But there is no decimal point in an integer.
# Python, just like in math, looks at the innermost parentheses first, and when it gets its answer, it continues to the next parentheses...
# 'float' allows you to type in numbers with decimal points as well. Can't have infinite decimals. 
# In programming in general, if something is in square brackets '[]', it means it's optional.
# The 'round' function rounds up the number to the nearest integer
# The 'return' function returns the value to us

def main():
    x = int(input("What's x? "))
    print("x sqaured is", square(x))

def square(n):
    return n * n # We have made a function which squares the number entered by the user, and then returns the value to us.



main()