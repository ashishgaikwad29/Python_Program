#   Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

Check = lambda No : No % 2 == 0

def main():
    Data = []

    num = int(input("Enter Number of Elements : "))

    for i  in range(num):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    fData = list(filter(Check,Data))

    print("Even Numbers are : ",fData)

if __name__ == "__main__":
    main()