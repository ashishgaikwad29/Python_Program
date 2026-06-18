# ============================================================
# Program 03 : Largest of Two Numbers
# ============================================================

# Problem Statement:
# Write a Python program that accepts two numbers
# from the user.
#
# Compare both numbers and display the larger number.
#
# If both numbers are equal,
# display:
# Both numbers are equal.
#
# Example:
#
# Input:
# Enter First Number  : 20
# Enter Second Number : 15
#
# Output:
# Largest Number : 20
#
# Example:
#
# Input:
# Enter First Number  : 50
# Enter Second Number : 50
#
# Output:
# Both numbers are equal.
# ============================================================

number1 = float(input("Enter First Number : "))
number2 = float(input("Enter Second Number : "))

if number1 > number2:
    print("Largest Number",number1)

elif number2 > number1:
    print("Largest Number : ",number2)

else:
    print("Both Numbers Are Equal ")
