# Task 1 - Identify the Greatest

print("=" * 50)
num1 = int(input("Type the first number:\n"))
print("=" * 50)
num2 = int(input("Type the second number:\n"))
print("=" * 50)
num3 = int(input("Type the third number:\n"))
print("=" * 50)
print("These are the numbers you have chosen:", num1, num2, num3)
print("=" * 50)

if num1 >= num2 and num1 >= num3:
    print("The largest number is", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is", num2)
elif num3 >= num1 and num3 >= num2:
    print("The largest number is", num3)