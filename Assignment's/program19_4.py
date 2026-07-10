# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square.
# Reduce will return addition of all that numbers.
#
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

even = lambda No : No % 2 == 0 
square = lambda No : No * No 
addition = lambda No1,No2 : No1 + No2

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]     
    print("-"*70)

    print("Input List : ",Data)
    print("-"*70)

    fData = list(filter(even,Data))
    print("List after filter : ",fData)
    print("-"*70)

    mData = list(map(square,fData))
    print("List after map : ",mData) 
    print("-"*70)

    rData = reduce(addition,mData)
    print("List after reduce : ",rData)
    print("-"*70)  

if __name__ == "__main__":
    main()