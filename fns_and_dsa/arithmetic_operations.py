# Defining the function
def perform_operation(num1, num2, operation):
    # Writing the statements
    if operation == 'add':
        return num1 + num2    #This adds two numbers
    elif operation == 'subtract':
        return num1 - num2    #This subtracts two numbers
    elif operation == 'multiply':
        return num1 * num2    #This multiplies two numbers
    elif operation == 'divide':
        if num2 == 0:
            return "Sorry, you cannot divide a number by zero."
        return num1 / num2    #This divides two numbers
    else:
        return "The operation is not Supported! Try Again."