# ============================================================
# Program 01 : Even or Odd
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts a number from the user.
#
# If the entered number is even,
# display:
# Even Number
#
# Otherwise, display:
# Odd Number
#
#
# Example:
#
# Input:
# Enter Number : 10
#
# Output:
# Even Number
#
# Example:
#
# Input:
# Enter Number : 7
#
# Output:
# Odd Number
# ============================================================

number = int(input("Enter the number to check : "))

if number % 2 == 0:
    print("Even Number :)")

else:
    print("Odd Number")