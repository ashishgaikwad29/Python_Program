# ============================================================
# Program 02 : Login System
# ============================================================

# Problem Statement:
# Write a Python program that accepts the username
# and password from the user.
#
# The valid credentials are:
#
# Username : admin
# Password : 1234
#
# If both the username and password are correct,
# display:
# Login Successful
#
# Otherwise, display:
# Invalid Username or Password
#
# Example:
#
# Input:
# Enter Username : admin
# Enter Password : 1234
#
# Output:
# Login Successful
#
# Example:
#
# Input:
# Enter Username : ashish
# Enter Password : 1234
#
# Output:
# Invalid Username or Password
# ============================================================

username = input("Enter Username : ")
password = int(input("Enter Password : "))

if username == "admin" and password == 1234:
    print("Login Successful")

else:
    print("Invalid Username or Password")