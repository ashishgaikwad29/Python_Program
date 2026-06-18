# ============================================================
# Program 03 : Divisible By 5
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts a number from the user.
#
# If the entered number is divisible by 5,
# display:
# Number is divisible by 5
#
# Example:
#
# Input:
# Enter Number : 25
#
# Output:
# Number is divisible by 5
# ============================================================

number = int(input("Enter Number To Check : "))

if number % 5 == 0:
    print("Number is divisible by 5 :) ")