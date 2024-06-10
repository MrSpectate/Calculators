# for loop
number = int(input("Please enter the table of the number you want here "))
z = int(input("Enter the size of the multiplication table (e.g., 10 for a 10x table"))
for n in range(1,z):
    print(number,"x",n,"=",number*n)

# while loop
number = int(input("Please enter the table of the number you want here "))
n  = 1 
while n < 11:
    print(number,"x",n,"=",number*n)
    n += 1