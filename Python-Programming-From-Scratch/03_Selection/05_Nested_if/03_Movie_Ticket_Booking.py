# ============================================================
# Program 03 : Movie Ticket Booking
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the user's age.
#
# If the user's age is 18 years or above,
# ask whether the user has a valid ID proof.
#
# If the ID proof is "yes",
# display:
# Ticket Booked
#
# Otherwise,
# display:
# ID Proof Required
#
# If the user is below 18 years,
# display:
# Not Eligible for Adult Movie
#
# Example:
#
# Input:
# Enter Age : 22
# Do you have a valid ID? (yes/no) : yes
#
# Output:
# Ticket Booked
# ============================================================

age = int(input("Enter Your Age : "))

if age >= 18:

    id_proof = input("Do you have a valid ID proof? (yes/no) : ")

    if id_proof == "yes":
        print("Ticket Booked")

    else:
        print("ID Proof Required")

else:
    print("Not Eligible for Adult Movie")