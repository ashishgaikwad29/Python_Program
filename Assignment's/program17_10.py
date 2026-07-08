# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934
# Output : 37

def AdditionDigits(No):
    Sum = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter Number : "))

    Ret = AdditionDigits(Value)

    print(Ret)

if __name__ == "__main__":
    main()