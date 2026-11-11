"""Practise variables, data types, input, and output."""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favourite_language = input("Enter your favourite programming language: ")

print("\n--- Your Details ---")
print("Name:", name)
print("Age:", age)
print("Favourite language:", favourite_language)
print("Age data type:", type(age).__name__)
