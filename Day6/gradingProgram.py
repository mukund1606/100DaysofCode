student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

students_grade = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        students_grade[student] = "Outstanding"
    elif score > 80:
        students_grade[student] = "Exceeds Expectations"
    elif score > 70:
        students_grade[student] = "Acceptable"
    else:
        students_grade[student] = "Fail"

print(students_grade)
