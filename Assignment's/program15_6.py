#   Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

Minimum = lambda No1,No2 : No1 if No1 < No2 else No2    # min(No1,No2)

def main():
    Data = []

    num = int(input("Enter Number of Elements Are : "))

    for i in range(num):
        Value = int(input("Enter number : "))
        Data.append(Value)

    Rdata = reduce(Minimum,Data)

    print("Minimum Number are : ",Rdata)        

if __name__ == "__main__":
    main()