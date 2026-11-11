"""A simple calculator using a function."""
def calculate(first, operator, second):
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        if second == 0:
            return "Error: division by zero is not allowed."
        return first / second
    else:
        return "Error: unsupported operator."

first_number = float(input("Enter the first number: "))
chosen_operator = input("Choose an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

print("Result:", calculate(first_number, chosen_operator, second_number))
