#    Write a lambda function which accepts one number and returns True if number is even otherwise False.

Check = lambda No : No % 2 == 0

def main():
    Value = int(input("Enter Number : "))

    Ret = Check(Value)

    if Ret == True:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()