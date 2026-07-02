#   Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number

Square = lambda No: No * No

def main():
    Data = []

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    MData = list(map(Square, Data))

    print("Input List  :", Data)
    print("Square List :", MData)

if __name__ == "__main__":
    main()