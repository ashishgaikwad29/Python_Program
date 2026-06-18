# ============================================================
# Program 03 : Basic Calculator
# ============================================================

# Problem Statement:
# Write a Python program that accepts two numbers
# and an operator (+, -, *, /) from the user.
#
# Perform the corresponding arithmetic operation
# based on the entered operator.
#
# If the operator is invalid,
# display:
# Invalid Operator
#
# Example:
#
# Input:
# Enter First Number  : 10
# Enter Second Number : 5
# Enter Operator      : +
#
# Output:
# Result : 15
#
# Example:
#
# Input:
# Enter Operator : %
#
# Output:
# Invalid Operator
# ============================================================

First_Number = float(input("Enter First Number : "))
Second_Number = float(input("Enter Second Number : "))
Operator = input(("Enter Your Operator : "))

if Operator == "+":
    no1 = First_Number + Second_Number
    print(no1)

elif Operator == "-":
    no2 = First_Number - Second_Number
    print(no2)

elif Operator == "/":
    no3 = First_Number / Second_Number
    print(no3)

elif Operator == "*":
    no3 = First_Number * Second_Number
    print(no3)

else:
    print("Enter Valid Operator")
