#  Task: Student Grades Categorization
# Objective:
# Write a Python program that processes a dictionary of student names and their exam scores,
# then generates a new dictionary with corresponding performance categories based on the score.
#
# Instructions:
# You are given a dictionary called student_scores that maps student names (str)
# to their numerical exam scores (int), ranging from 0 to 100.
# Create a new dictionary called student_grades.

# Iterate over each student in student_scores and assign a grade category to student_grades according to the following rules:
# Scores above 90 and up to 100 → "Outstanding"
# Scores above 80 and up to 90 → "Exceeds Expectations"
# Scores above 70 and up to 80 → "Acceptable"
# Scores 70 or below → "Fail"
#
# Print the resulting student_grades dictionary at the end.

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if 90 < score <= 100:
        student_grades[key] = "Outstanding"
    elif 80 < score <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 70 < score <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
# or
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
