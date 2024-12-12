def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False
    
a = 2  # Initial value for a
b = 3  # Initial value for b

result = greaterThan(a, b)

print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

a = 10  # Change the value of a
b = 6   # Change the value of b

result = greaterThan(a, b)

print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
