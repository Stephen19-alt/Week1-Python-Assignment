# Function for Addition
def add(num1, num2):
    return num1 + num2

# Function for Substraction
def sub(num1, num2):
    return num1 - num2

# Function for Multiplication
def mul(num1, num2):
    return num1 * num2

# Function for Division
def div(num1, num2):
    return num1 / num2

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

# Take input from the user
operation = int(input("Select operation (1-4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif operation == 3:
    print(num1, "*", num2, "=", mul(num1, num2))
elif oprration == 4:
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("Invalid input")
