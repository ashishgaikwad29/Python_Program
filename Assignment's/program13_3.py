# Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def Check(No):
    Total = 0

    for i in range(1, No):
        if No % i == 0:
            Total = Total + i

    if Total == No:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

def main():
    Value = int(input("Enter Number : "))

    Check(Value)

if __name__ == "__main__":
    main()