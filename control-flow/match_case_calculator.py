#Ask the user to enter two numbers:

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        print("The result is", num1 + num2)
    case "-":
        print("The result is", num1 - num2)
    case "*":
        print("The result is", num1 * num2)
    case "/":
        if num1 or num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is", num1 / num2)
    case _:
        print("Invalid Operation")