# Write a program which accepts one number and prints binary equivalent.

def Binary(No):
    Result = ""

    while No > 0:
        Digit = No % 2
        Result = str(Digit) + Result
        No = No // 2

    return Result

def main():
    Value = int(input("Enter Number : "))

    Ret = Binary(Value)

    print("Binary Equivalent is :", Ret)

if __name__ == "__main__":
    main()