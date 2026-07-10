# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
#
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def Check_Prime(No):
    Count = 0

    for i in range(1, No + 1):
        if No % i == 0:
            Count = Count + 1

    if Count == 2:
        return True
    else:
        return False

Mult = lambda No : No * 2

Maximum = lambda No1,No2 : max(No1,No2) 

def main():

    print("-"*70)
    Get = int(input("Enter Number of Elements : "))
    print("-"*70)

    Data = list(map(int, input("Enter Numbers : ").split()))
    print("-"*70)

    print("Input List : ", Data)
    print("-"*70)

    fData = list(filter(Check_Prime,Data))
    print("List after filter : ",fData)
    print("-"*70)

    mData = list(map(Mult,fData))
    print("List after map : ",mData)
    print("-"*70)

    rData = reduce(Maximum,mData)
    print("Output of reduce : ",rData)
    print("-"*70)

if __name__ == "__main__":
    main()