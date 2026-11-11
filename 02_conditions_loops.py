"""Practise conditions and loops."""
number = int(input("Enter an integer: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("\nMultiplication table:")
for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")

print("\nCounting from 1 to 5:")
count = 1
while count <= 5:
    print(count)
    count += 1
