# Range Function with 3 arguments
# Enter number from which we have to start
num1 = int(input("Enter First Number = "))
# Enter a number where to end
num2 = int(input("Enter Second Number = "))
# Enter a number to take difference between the numbers
num3 = int(input("Enter Number to take difference = "))
numbers = list(range(num1, num2,num3))
print(numbers)
