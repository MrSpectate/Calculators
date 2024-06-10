
print("__CALCULATOR__")
# def using for add
def add(a,b):
    c = a + b
    return c

# def using for subtract
def subtract(a,b):
    c = a - b
    return c
# def using for divide
def divide(a,b):
    c =  a / b
    return c

# def using for multiply
def multiply(a,b):
    c = a*b
    return c

# def using for square or power
def power(a,b):
    c = a**b
    return c
# def using for percentage
def percentage(a,b):
    c = a/b * 100
    return c

# Enter 1st integer
a = int(input("Enter a  first number : "))

#  Select an operators( -,+,/,*)
operation = input("Enter the operation : ")

# Enter 2nd integer
b = int(input("Enter a second number : "))

# Perform the calculation based on the operator
if operation == "+" :
    print(add(a,b))
elif operation == "_":
    print(subtract(a,b))
elif operation == "*":
    print(multiply(a,b))
elif operation == "/":
    print(divide(a,b))
elif operation == "**":
    print(power(a**b))
elif operation == "%":
    print(percentage(a,b)) 

else:
    print("Barwe sai operation select kar !")

