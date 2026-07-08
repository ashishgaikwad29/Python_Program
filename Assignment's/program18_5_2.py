# Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 + 2 + 5)

import program18_5_1

def ListPrime(Data):
    Sum = 0

    for i in Data:
        if program18_5_1.ChkPrime(i):
            Sum = Sum + i

    return Sum

def main():
    Data = []

    Size = int(input("Enter Number of Elements : "))

    for i in range(Size):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    Ret = ListPrime(Data)

    print(Ret)

if __name__ == "__main__":
    main()