# Write a program that counts how many odd numbers exist between 1 and N.

from multiprocessing import Pool
import os

def CountOdd(No):
    Count = (No + 1) // 2
    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Odd Number Count :", Count)
    print("-" * 30)
    return Count

def main():
    Data = list(map(int, input("Enter Numbers : ").split()))
    with Pool() as P:
        P.map(CountOdd, Data)

if __name__ == "__main__":
    main()
