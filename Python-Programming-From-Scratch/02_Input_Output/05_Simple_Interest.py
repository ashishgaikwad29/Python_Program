# ============================================================
# Program 05 : Simple Interest Calculator
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the Principal Amount,
# Rate of Interest, and Time from the user.
#
# Calculate the Simple Interest using the formula:
#
# Simple Interest = (Principal × Rate × Time) / 100
#
# Display the calculated Simple Interest.
#
# ============================================================

Principal_Amount = int(input("Enter Principle Amount : "))
Rate_of_Interest = int(input(("Enter Rate Of Interest : ")))
Time = int(input("Enter Time : "))

Simple_Interest = (Principal_Amount * Rate_of_Interest * Time) / 100


print("Calculated Simple Interest is : ",Simple_Interest)