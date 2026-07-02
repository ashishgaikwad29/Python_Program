#    Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

Check = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    Data = []

    Count = int(input("Enter Number of Elements : "))

    for i in range(Count):
        Value = int(input("Enter Number : "))
        Data.append(Value)

    Fdata = list(filter(Check,Data))

    print("Numbers which are divisible by 3 and 5 are : ",Fdata)        

if __name__ == "__main__":
    main()