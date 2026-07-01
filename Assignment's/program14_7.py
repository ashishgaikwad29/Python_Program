#    Write a lambda function which accepts one number and returns True if divisible by 5.

Div = lambda No : No % 5 == 0

def main():
    Value = int(input("Enter Number : "))
        
    Ret = Div(Value)

    if Ret == True:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()