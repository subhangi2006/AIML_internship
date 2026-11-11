"""Practise list indexing and list operations."""
subjects = ["Python", "Mathematics", "Artificial Intelligence"]

print("Original list:", subjects)
print("First subject:", subjects[0])

new_subject = input("Enter one more subject: ")
subjects.append(new_subject)

print("Updated list:", subjects)
print("Number of subjects:", len(subjects))

subjects.sort()
print("Sorted list:", subjects)
