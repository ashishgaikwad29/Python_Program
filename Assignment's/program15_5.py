#   Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

Maximum = lambda No1,No2 : No1 if No1 > No2 else No2    # max(No1,No2)

def main():
    Data = []

    num = int(input("Enter Number of Elements : "))

    for i in range(num):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    Rdata = reduce(Maximum,Data)

    print("Maximum Numbers are : ",Rdata)

if __name__ == "__main__":
    main()