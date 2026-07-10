# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers.
#
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

fList = lambda No : No >= 70 and No <= 90
mList = lambda No : No + 10
rList = lambda No1,No2 : No1 * No2

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]  
    print("-"*70)

    print("Inpute List is : ",Data)
    print("-"*70) 

    fData = list(filter(fList,Data))
    print("List after filter : ",fData) 
    print("-"*70) 

    mData = list(map(mList,fData)) 
    print("List after map : ",mData)  
    print("-"*70)

    rData = (reduce(rList,mData))
    print("List after reduce : ",rData)
    print("-"*70)

if __name__ == "__main__":
    main()