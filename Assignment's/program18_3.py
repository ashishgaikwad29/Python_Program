# Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def Minimum(Data):
    Min = Data[0]

    for i in Data:
        if i < Min:
            Min = i

    return Min

def main():
    Data = []

    Size = int(input("Enter Number of Elements : "))

    for i in range(Size):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    Ret = Minimum(Data)

    print(Ret)

if __name__ == "__main__":
    main()