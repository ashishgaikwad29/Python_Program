# Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def Frequency(Data, No):
    Count = 0

    for i in Data:
        if i == No:
            Count = Count + 1

    return Count

def main():
    Data = []

    Size = int(input("Enter Number of Elements : "))

    for i in range(Size):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    Search = int(input("Enter Element to Search : "))

    Ret = Frequency(Data, Search)

    print(Ret)

if __name__ == "__main__":
    main()