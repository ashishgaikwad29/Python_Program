# ============================================================
# Program 01 : Scholarship Eligibility
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the student's
# marks and annual family income.
#
# A student is eligible for a scholarship only if:
#
# - Marks are 85 or above.
# - Annual family income is less than or equal to ₹300000.
#
# If both conditions are satisfied,
# display:
# Scholarship Approved
#
# Otherwise, display:
# Scholarship Not Approved
#
# Example:
#
# Input:
# Enter Marks          : 90
# Enter Annual Income  : 250000
#
# Output:
# Scholarship Approved
#
# Example:
#
# Input:
# Enter Marks          : 90
# Enter Annual Income  : 500000
#
# Output:
# Scholarship Not Approved
# ============================================================

marks = float(input("Enter Your Marks : "))
annual_income = float(input("Enter Family Income : "))

if marks >= 85 and annual_income <= 300000:
    print("Eligible for Scolarship :) ")

else:
    print("Scholarship Not Approved :(")