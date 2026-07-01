#   Write a program which accepts one number and checks whether it is prime or not.
#   Input: 11 
#   Output: Prime Number

def prime(No):
    if No <= 1:
        print("Not Prime Number")
    else:
        for i in range(2, int(No**0.5) + 1):
            if No % i == 0:
                print("Not Prime Number")
                return
        print("Prime Number")
        
def main():
    Value = int(input("Enter Number : "))

    prime(Value)

if __name__ == "__main__":
    main()