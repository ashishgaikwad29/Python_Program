# ============================================================
# Program 02 : Bank Loan Approval
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the user's
# monthly salary and credit score.
#
# The bank should first check whether the monthly
# salary is ₹30000 or more.
#
# If the salary condition is satisfied,
# then check the credit score.
#
# If the credit score is 750 or above,
# display:
# Loan Approved
#
# Otherwise, display:
# Low Credit Score
#
# If the salary is less than ₹30000,
# display:
# Salary Criteria Not Met
#
# Example:
#
# Input:
# Enter Monthly Salary : 45000
# Enter Credit Score : 780
#
# Output:
# Loan Approved
# ============================================================

salary = int(input("Enter your monthly salary : "))
credit_score = float(input("Enter Your Credit Score : "))

if salary >= 30000:
    if credit_score >= 750:
        print("Loan Approved ")

    else:
        print("Low Credit Score ")

else:
    print("Salary Criteria Not Met")