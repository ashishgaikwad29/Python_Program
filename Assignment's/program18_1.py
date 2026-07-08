# Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def Addition(Data):
    Sum = 0

    for i in Data:
        Sum = Sum + i

    return Sum

def main():
    Data = []

    Size = int(input("Enter Number of Elements : "))

    for i in range(Size):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    Ret = Addition(Data)

    print(Ret)

if __name__ == "__main__":
    main()