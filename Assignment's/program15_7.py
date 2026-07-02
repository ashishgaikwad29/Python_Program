#   Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

Check = lambda Name : len(Name) > 5

def main():
    Data = []

    Count = int(input("Enter Elements : "))

    for i in range(Count):
        num = input("Enter Name : ")
        Data.append(num)

    Fdata = list(filter(Check,Data))

    print("Largest Name In the string is : ",Fdata)

if __name__ == "__main__":
    main()