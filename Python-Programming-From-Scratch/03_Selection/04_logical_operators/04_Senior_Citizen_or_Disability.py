# ============================================================
# Program 04 : Senior Citizen or Disability
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts a person's
# age and disability status.
#
# A person is eligible for government assistance if:
#
# - Age is 60 years or above.
# OR
# - The person has a disability.
#
# If either condition is true,
# display:
# Eligible for Government Assistance
#
# Otherwise, display:
# Not Eligible
#
# Note:
# For disability status, enter:
# yes
# no
#
# Example:
#
# Input:
# Enter Age : 30
# Disability (yes/no) : yes
#
# Output:
# Eligible for Government Assistance
# ============================================================


age = int(input("Enter Your Age : "))
disablity = (input("Disability (yes/no) : "))

if age >= 60 or disablity == "yes":
    print("Eligible for Government Assistance")
else:
    print("Not Eligible")