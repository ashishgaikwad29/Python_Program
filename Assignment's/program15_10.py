#   Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

Check = lambda No : No % 2 == 0 

def main():
    Data = []

    Count = int(input("Enter Number of Elements : "))

    for i in range(Count):
        value = int(input("Enter Numbers : "))
        Data.append(value)

    Fdata = list(filter(Check,Data))

    print("Count is : ",len(Fdata))

    print("Even numbers are : ",Fdata)        

if __name__ == "__main__":
    main()