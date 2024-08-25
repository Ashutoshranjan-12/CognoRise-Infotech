# CALCULATOR APP

def Calculator():
    # Prompt the user to select an operation
    operator = input("Select the operation (+, -, *, /): ")
    
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the operation based on user input
    if operator == "+":
        # Calculate the sum if the operator is '+'
        result = num1 + num2
        print(f"The sum of {num1} + {num2} = {result}")
    
    elif operator == "-":
        # Calculate the difference if the operator is '-'
        result = num1 - num2
        print(f"The difference of {num1} - {num2} = {result}")
    
    elif operator == "*":
        # Calculate the product if the operator is '*'
        result = num1 * num2
        print(f"The product of {num1} * {num2} = {result}")
    
    elif operator == "/":
        # Calculate the quotient if the operator is '/'
        if num2 != 0:
            # Check for division by zero
            result = num1 / num2
            print(f"The quotient of {num1} / {num2} = {result}")
        else:
            # Print an error message if division by zero is attempted
            print("Error! Division by zero is not possible.")
    
    else:
        # Print an error message for invalid operators
        print("Enter a valid operator!")

# Call the Calculator function to execute the code
Calculator()