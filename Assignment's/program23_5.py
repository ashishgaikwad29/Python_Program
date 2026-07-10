# Write a program that calculates factorials of multiple numbers
# simultaneously using multiprocessing.Pool.

from multiprocessing import Pool
import math
import os

def Factorial(No):
    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Factorial :", math.factorial(No))
    print("-" * 30)
    return math.factorial(No)

def main():
    Data = list(map(int, input("Enter Numbers : ").split()))
    with Pool() as P:
        P.map(Factorial, Data)

if __name__ == "__main__":
    main()
