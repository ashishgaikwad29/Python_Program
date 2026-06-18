# ============================================================
# Program 01 : Grade Calculator
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the marks
# obtained by a student.
#
# Display the grade according to the following criteria:
#
# Marks >= 90       : Grade A
# Marks >= 75       : Grade B
# Marks >= 60       : Grade C
# Marks >= 35       : Grade D
# Marks < 35        : Fail
#
# Example:
#
# Input:
# Enter Marks : 82
#
# Output:
# Grade B
# ============================================================

marks = float(input("Enter Your Marks : "))

if marks >= 90:
    print("Grade A ")

elif marks >= 75:
    print("Grade B ")

elif marks >= 60:
    print("Grade C ")

elif marks >= 35:
    print("Grade D ")

else:
    print("Fail :(")
