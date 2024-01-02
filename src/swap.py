# working of how to take an input from the User.

num1 = input("Enter the first number \n")
num2 = input("Enter the second number \n")

print("numbers before Swapping: \n")
print("The value of num1 is: ", num1)
print("The value of num2 is: ", num2)

temp = num1
num1 = num2
num2 = temp

print("numbers after Swapping: \n")
print("The value of num1 is: ", num1)
print("The value of num2 is: ", num2)
