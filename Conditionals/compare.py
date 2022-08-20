x = int(input("What's x? "))
y = int(input("What's y? "))

# If the first part of the if function is not true it will check the other part, that comes after or. If neither are true, it will print the else statement
if x < y or x > y: 
    print("x is not equal to y")
else:
    print("x is equal to y")