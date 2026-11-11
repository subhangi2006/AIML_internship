"""Practise defining and calling functions."""
def greet(name):
    return f"Hello, {name}! Welcome to Python."

def add(first_number, second_number):
    return first_number + second_number

person = input("Enter your name: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

print(greet(person))
print("Sum:", add(first, second))
