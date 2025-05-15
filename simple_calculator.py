# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide the first number by the second
def divide(a, b):
    try:
        return a / b  # Try to perform division
    except ZeroDivisionError:  # Handle division by zero error
        return "Error: Cannot divide by zero."

# Main function that runs the calculator
def main():
    print("Welcome to Simple Calculator")
    
    try:
        # Get first number from the user and convert it to float
        num1 = float(input("Enter first number: "))
        # Get second number from the user and convert it to float
        num2 = float(input("Enter second number: "))
    except ValueError:  # Handle input that is not a number
        print("Invalid input. Please enter numeric values.")
        return  # Exit the function early if input is invalid

    # Ask user to select an operation
    print("Select operation: +  -  *  /")
    operation = input("Enter operation: ")

    # Perform the operation based on user input
    if operation == '+':
        print("Result:", add(num1, num2))
    elif operation == '-':
        print("Result:", subtract(num1, num2))
    elif operation == '*':
        print("Result:", multiply(num1, num2))
    elif operation == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation selected.")  # Handle invalid operation input

# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    main()
