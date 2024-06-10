import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def power(a, b):
    return math.pow(a, b)

def square_root(a):
    return math.sqrt(a)

def logarithm(a, base=10):
    return math.log(a, base)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def factorial(a):
    return math.factorial(a)

def scientific_calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sin")
    print("9. Cos")
    print("10. Tant")
    print("11. Factorial")

    choice = input("Enter choice (1-11): ")

    if choice in ['1', '2', '3', '4', '5', '7']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    
    if choice == '6' or choice in ['8', '9', '10', '11']:
        num = int(input("Enter number: "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {power(num1, num2)}")
    elif choice == '6':
        print(f"Result: {square_root(num)}")
    elif choice == '7':
        base = int(input("Enter logarithm base: "))
        print(f"Result: {logarithm(num1, base)}")
    elif choice == '8':
        print(f"Result: {sine(num)}")
    elif choice == '9':
        print(f"Result: {cosine(num)}")
    elif choice == '10':
        print(f"Result: {tangent(num)}")
    elif choice == '11':
        print(f"Result: {factorial(int(num))}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    scientific_calculator()
