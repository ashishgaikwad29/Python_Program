# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4       3       Output : 12
# Input : 6       3       Output : 18

mult = lambda No1,No2 : No1 * No2

def main():
    Get1 = int(input("Enter First Number : "))
    Get2 = int(input("Enter Second Number : "))

    Ans = mult(Get1,Get2)

    print(f"Multiplication of {Get1} and {Get2} is : ",Ans)        

if __name__ == "__main__":
    main()