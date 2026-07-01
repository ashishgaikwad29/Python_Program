#   Write a program which accepts one number and checks whether it is palindrome or not.
#   Input: 121 
#   Output: Palindrome

def Palindrome(No):
    Temp = No
    Rev = 0

    while No > 0:
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10

    if Temp == Rev:
        return True
    else:
        return False

def main():
    Value = int(input("Enter Number : "))

    Ret = Palindrome(Value)

    if Ret == True:
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

if __name__ == "__main__":
    main()