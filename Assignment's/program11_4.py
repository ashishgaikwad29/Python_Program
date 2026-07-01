# Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def Change(No1):
    Rev = 0

    while No1 > 0:
        Digit = No1 % 10
        Rev = (Rev * 10) + Digit
        No1 = No1 // 10

    return Rev

def main():
    Value = int(input("Enter Number : "))

    Ret = Change(Value)

    print("Reverse Number is :", Ret)

if __name__ == "__main__":
    main()