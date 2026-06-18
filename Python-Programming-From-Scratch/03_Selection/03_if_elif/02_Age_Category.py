# ============================================================
# Program 02 : Age Category
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts a person's age.
#
# Display the category according to the following criteria:
#
# Age = 60       : Senior Citizen
# Age = 18       : Adult
# Age = 13       : Teenager
# Otherwise      : Child
#
# Example:
#
# Input:
# Enter Age : 25
#
# Output:
# Adult
#
# Example:
#
# Input:
# Enter Age : 10
#
# Output:
# Child
# ============================================================

age = int(input("Enter Your Age : "))

if age >= 60:
    print("Senior Citizen")

elif age >= 18:
    print("Adult")

elif age >=13:
    print("Teenager")

else:
    print("Child")
    