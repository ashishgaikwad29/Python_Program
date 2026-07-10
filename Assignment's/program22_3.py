# Write a program that counts how many prime numbers
# exist between 1 and N using multiprocessing Pool.

from multiprocessing import Pool
import os

def CountPrime(No):
    Count = 0
    for i in range(2, No + 1):
        Prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                Prime = False
                break
        if Prime:
            Count += 1
    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Prime Count :", Count)
    print("-" * 30)
    return Count

def main():
    Data = list(map(int, input("Enter Numbers : ").split()))
    with Pool() as P:
        P.map(CountPrime, Data)

if __name__ == "__main__":
    main()
