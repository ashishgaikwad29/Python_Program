# Write a program that counts how many even numbers exist between 1 and N using Pool.map().

from multiprocessing import Pool
import os

def CountEven(No):
    Count = No // 2
    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Even Number Count :", Count)
    print("-" * 30)
    return Count

def main():
    Data = list(map(int, input("Enter Numbers : ").split()))
    with Pool() as P:
        P.map(CountEven, Data)

if __name__ == "__main__":
    main()
