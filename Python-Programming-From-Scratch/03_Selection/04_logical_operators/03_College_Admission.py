# ============================================================
# Program 03 : College Admission
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the student's
# percentage and entrance exam score.
#
# A student gets admission only if:
#
# - Percentage is 60 or above.
# - Entrance Exam Score is 120 or above.
#
# If both conditions are satisfied,
# display:
# Admission Granted
#
# Otherwise, display:
# Admission Denied
#
# Example:
#
# Input:
# Enter Percentage : 75
# Enter Entrance Exam Score : 130
#
# Output:
# Admission Granted
#
# ============================================================


percentage = float(input("Enter Percentages : "))
entrance_exam_score = float(input("Entrance Exam Score : "))

if percentage >= 60 and entrance_exam_score >= 120:
    print("Admission Granted :)")

else:
    print("Admission Denied :( ")