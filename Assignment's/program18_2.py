# Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def Maximum(Data):
    Max = Data[0]

    for i in Data:
        if i > Max:
            Max = i

    return Max

def main():
    Data = []

    Size = int(input("Enter Number of Elements : "))

    for i in range(Size):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    Ret = Maximum(Data)

    print(Ret)

if __name__ == "__main__":
    main()