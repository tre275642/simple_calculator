def simple_calculator():
    print("Welcome to the simple Python calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num1 or num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use one of these: +, -, *, /")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    simple_calculator()