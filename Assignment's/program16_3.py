#   Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers. 
#   Input : 11    5   
#   Output : 16 

def Add(No1,No2):
    return No1 + No2

def main():
    num1 = int(input("Enter First Number  : ")) 
    num2 = int(input("Enter Second Number : ")) 

    Ret = Add(num1,num2)

    print("Addition of two numbers is : ",Ret)

if __name__ == "__main__":
    main()