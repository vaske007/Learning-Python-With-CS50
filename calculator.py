# 'int', which is short for integers, is a number all the way toward negative infinity, and all the way toward positive infinity. But there is no decimal point in an integer.
# Python, just like in math, looks at the innermost parentheses first, and when it gets its answer, it continues to the next parentheses...
# 'float' allows you to type in numbers with decimal points as well. Can't have infinite decimals. 
# In programming in general, if something is in square brackets '[]', it means it's optional.
# The 'round' function rounds up the number to the nearest integer

x = float(input("What's x? ")) # Input function gets called first and then the result of that becomes the input to the float function
y = float(input("What's y? ")) # Input function gets called first and then the result of that becomes the input to the float function

z = round(x +y)

print(f"{z: ,}") # Puts a comma every three numbers
