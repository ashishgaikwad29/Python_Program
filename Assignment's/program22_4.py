# Write a program that calculates
# 1^5+2^5+3^5+.....+N^5
# for multiple values of N simultaneously using Pool.
# Measure total execution time.

from multiprocessing import Pool
import time

def SumPower(No):
    Sum = 0
    for i in range(1, No + 1):
        Sum += i ** 5
    return Sum

def main():
    Data = list(map(int, input("Enter Numbers : ").split()))

    Start = time.time()

    with Pool() as P:
        Result = P.map(SumPower, Data)

    End = time.time()

    print(Result)
    print("Execution Time :", End - Start)

if __name__ == "__main__":
    main()
