# Write a program which accept one number from user and return its factorial.
# Input : 5
# Output : 120

def Factorial(No):
    Fact = 1

    for i in range(No, 0, -1):
        Fact = Fact * i

    return Fact

def main():
    Value = int(input("Enter Number : "))

    Ret = Factorial(Value)

    print(Ret)

if __name__ == "__main__":
    main()