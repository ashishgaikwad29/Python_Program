# Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def Sum(No):
    Addition = 0

    while No > 0:
        Digit = No % 10
        Addition = Addition + Digit
        No = No // 10

    return Addition

def main():
    Value = int(input("Enter Number : "))

    Ret = Sum(Value)

    print("Addition is :", Ret)

if __name__ == "__main__":
    main()