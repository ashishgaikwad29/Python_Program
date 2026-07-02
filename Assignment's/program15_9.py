#    Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

Product = lambda No1,No2 : No1 * No2

def main():
    Data = []

    Count = int(input("Enter Number of Elements : "))

    for i in range(Count):
        value = int(input("Enter Numbers : "))
        Data.append(value)

    Fdata = reduce(Product,Data)

    print("Product of all elements are : ",Fdata)       

if __name__ == "__main__":
    main()