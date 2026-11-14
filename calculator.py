
# =================================
#       PYTHON CALCULATOR
#       Created by: Kedar
# =================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a % b


while True:
    print("\n====== PYTHON CALCULATOR ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")

    choice = input("\nChoose an operation (1-6): ")

    if choice == "6":
        print("Thank you for using my calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice! Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = modulus(num1, num2)

        print("\nResult:", result)

    except ValueError:
        print("Please enter valid numbers!")
