print("Select an operation to perform: ")
print("1, Add")
print("2, Subtarct")
print("3, Multiply")
print("4, Division")

operation = input()
if operation == "1":
  num1 = input("Enter first number:")
  num2 = input("Enter second number:")
  print("the sum is " + str(int(num1) + int(num2)))
elif operation == "2":
  num1 = input("Enter first number:")
  num2 = input("Enter second number:")
  print("the sum is " + str(int(num1) - int(num2)))
elif operation == "3":
  num1 = input("Enter first number:")
  num2 = input("Enter second number:")
  print("the sum is " + str(int(num1) * int(num2)))
elif operation == "4":
  num1 = input("Enter first number:")
  num2 = input("Enter second number:")
  print("the sum is " + str(int(num1) / int(num2)))
else:
  print("INVALID ENTRY")