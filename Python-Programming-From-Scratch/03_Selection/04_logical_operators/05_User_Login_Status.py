# ============================================================
# Program 05 : User Login Status
# ============================================================

# Problem Statement:
# Write a Python program that accepts the user's
# login status.
#
# The user should enter:
# yes
# no
#
# If the user is NOT logged in,
# display:
# Please Login
#
# Otherwise, display:
# Welcome Back
#
# Note:
# Use the 'not' logical operator.
#
# Example:
#
# Input:
# Are you logged in? (yes/no) : no
#
# Output:
# Please Login
#
# Example:
#
# Input:
# Are you logged in? (yes/no) : yes
#
# Output:
# Welcome Back
# ============================================================

Status = input("Are you logged in? (yes/no)")

log = Status == "yes"

if not log:
    print("Please login")
else:
    print("Welcome Back")