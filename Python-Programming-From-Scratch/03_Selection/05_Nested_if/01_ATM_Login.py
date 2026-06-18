# ============================================================
# Program 01 : ATM Login
# ============================================================

# Problem Statement:
# Write a Python program that accepts the ATM card
# status and PIN from the user.
#
# The ATM should first check whether the card is valid.
#
# If the card is valid, then ask the user to enter the PIN.
#
# If the entered PIN is 1234,
# display:
# Login Successful
#
# Otherwise, display:
# Invalid PIN
#
# If the card is not valid,
# display:
# Invalid ATM Card
#
# Example:
#
# Input:
# Is your ATM card valid? (yes/no) : yes
# Enter PIN : 1234
#
# Output:
# Login Successful
#
# Example:
#
# Input:
# Is your ATM card valid? (yes/no) : yes
# Enter PIN : 1111
#
# Output:
# Invalid PIN
#
# Example:
#
# Input:
# Is your ATM card valid? (yes/no) : no
#
# Output:
# Invalid ATM Card
# ============================================================

card = input("Is your ATM card valid? (yes/no) : ")

if card == "yes":

    pin = int(input("Enter PIN : "))

    if pin == 1234:
        print("Login Successful")

    else:
        print("Invalid PIN")

else:
    print("Invalid ATM Card")