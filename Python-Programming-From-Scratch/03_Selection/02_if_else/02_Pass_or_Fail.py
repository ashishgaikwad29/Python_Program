# ============================================================
# Program 02 : Pass or Fail
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the marks obtained
# by a student.
#
# If the marks are 35 or more,
# display:
# Pass
#
# Otherwise, display:
# Fail
#
# Example:
#
# Input:
# Enter Marks : 75
#
# Output:
# Pass
#
# Example:
#
# Input:
# Enter Marks : 20
#
# Output:
# Fail
# ============================================================

marks = float(input("Enter Your Marks :"))

if marks >= 35:
    print("Pass :)")

else:
    print("Fail :(")