def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by 0 is not allowed"
    else:
        return num1 / num2

num1 = float(input("Enter first number :  "))
num2 = float(input("Enter second number : "))

print("Select Operation :")
print("+. Addition")
print("-. Subtraction")
print("*. Multiply")
print("/. Divide")

choice = input("Enter the Operation needed :")
if choice in ('+', '-', '*', '/'):
    if choice == '+':
        print("Result of Sum is : ", add(num1, num2))
    elif choice == '-':
        print("Result of Subtract is : ",subtract(num1, num2))
    elif choice == '*':
        print("Result of Multiply is : ",multiply(num1, num2))
    elif choice == '/':
        print("Result of Divide is : ",divide(num1, num2))
else:
    print("Invalid input")
