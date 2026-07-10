# Write a program that accepts a list of integers and uses Pool.map()
# to calculate the sum of squares from 1 to N for every element in the list.

from multiprocessing import Pool

def SumSquare(No):
    Sum = 0
    for i in range(1, No + 1):
        Sum += i * i
    return Sum

def main():
    Data = list(map(int, input("Enter Numbers : ").split()))

    with Pool() as P:
        Result = P.map(SumSquare, Data)

    print(Result)

if __name__ == "__main__":
    main()
