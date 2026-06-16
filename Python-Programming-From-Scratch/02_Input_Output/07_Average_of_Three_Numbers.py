# ============================================================
# Program 07 : Average of Three Numbers
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts three numbers
# from the user.
#
# Calculate the average of the three numbers and
# display the result.
#
# Formula:
# Average = (Number1 + Number2 + Number3) / 3
#
# Example:
#
# Input:
# Enter First Number  : 10
# Enter Second Number : 20
# Enter Third Number  : 30
#
# Output:
# Average : 20.0
#
# ============================================================

No1 = float(input("Enter First Number  : "))
No2 = float(input("Enter Second Number : "))
No3 = float(input("Enter Third Number  : "))

average = (No1 + No2 + No3) / 3

print("Your Average of three number is : ",average)