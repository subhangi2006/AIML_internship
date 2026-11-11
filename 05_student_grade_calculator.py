"""Calculate average marks and assign a simple grade."""
number_of_subjects = int(input("Enter the number of subjects: "))

if number_of_subjects <= 0:
    print("Please enter at least one subject.")
    raise SystemExit

marks = []
for index in range(number_of_subjects):
    mark = float(input(f"Enter marks for subject {index + 1} (0-100): "))
    if not 0 <= mark <= 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        raise SystemExit
    marks.append(mark)

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("\nMarks:", marks)
print(f"Average: {average:.2f}")
print("Grade:", grade)
