print("\n__CALCULATOR__\n")


# Enter an 1st integer
num_1 = int(input("Enter the first digit : "))

# Select an operators( -,+,/,*)
print("+,-,*,/")
operator = (input("Enter the operator that you want to perform : "))

# Enter an 2nd integer
num_2 = int(input("Enter the second digit : "))

# Perform the calculation based on the operator
if operator == "+":
    print(num_1 + num_2)
elif (operator == "-"):
    print(num_1 - num_2)
elif (operator == "*"):
    print(num_1 * num_2)
elif (operator == "/"):
    print(num_1 / num_2)
else:
    print("Invaild Input")