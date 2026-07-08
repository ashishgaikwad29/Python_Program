# ------------------------------------------------------------
# File Name   : Assignment17_2.py
# Author      : Ashish Gaikwad
# Description : Display star pattern.
#
# Question:
# Write a program which accepts one number and displays
# the following pattern.
#
# Input : 5
#
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# ------------------------------------------------------------

def Pattern(No):
    for i in range(No):
        for j in range(No):
            print("*", end=" ")
        print()

def main():
    Value = int(input("Enter Number : "))

    Pattern(Value)

if __name__ == "__main__":
    main()