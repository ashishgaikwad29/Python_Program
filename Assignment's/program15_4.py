#   Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

Add = lambda No1,No2 : No1 + No2

def main():
    Data = []

    num = int(input("Enter Number Of Element's : "))

    for i in range(num):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    Fdata = reduce(Add,Data)

    print("Addition are : ",Fdata)        

if __name__ == "__main__":
    main()