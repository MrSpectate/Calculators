



print("\n__CALCULATOR__\n")

# Enter 1st integer
num_1 = int(input("Enter the first number: "))

# Select an operators( -,+,/,*)
print("+, -, *, /, **, %")
operator = input("Enter the operator that you want to perform: ")

# Enter 2nd integer
num_2 = int(input("Enter the second number: "))

# Perform the calculation based on the operator
if operator == "**":
    result = num_1 ** num_2
    print(f"The result of {num_1} ** {num_2} is: {result}")
elif operator == "-":
    result = num_1 - num_2
    print(f"The result of {num_1} - {num_2} is: {result}")
elif operator == "*":
    result = num_1 * num_2
    print(f"The result of {num_1} * {num_2} is: {result}")
elif operator == "/":
    result = num_1 / num_2
    print(f"The result of {num_1} / {num_2} is: {result}")
elif operator == "%":
    result = num_1 % num_2
    print("The result is ", (num_1 / num_2) * 100 )
elif (operator == "+"):
    result = num_1 + num_2
    print(f"The result of {num_1} + {num_2} is : {result}")
else:   
    print("Invalid Input")
    
