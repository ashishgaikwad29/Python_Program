# ============================================================
# Program 02 : Future Age Calculator
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the user's name and
# current age from the keyboard.
#
# Calculate the user's age after 5 years and display it in
# the following format:
# Output:
# Hello <name>, after 5 years you will be <future_age> years old.

Name = 0
Age = 0

print("Enter Your Name")
Name = input()

print("Enter Your Age ")
Age = int(input())

print("Hello",Name,"after 5 years you will be",Age + 5 ,"years old.")
