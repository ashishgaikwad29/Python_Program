#   Write a program which accepts one number and prints count of digits in that number.
#   Input: 7521 
#   Output: 4

def Count(No):
    count = 0

    while No > 0:
        count = count + 1
        No = No // 10

    return count

def main():
    Value = int(input("Enter number: "))

    Ret = Count(Value)

    print("Count is:", Ret)

if __name__ == "__main__":
    main()