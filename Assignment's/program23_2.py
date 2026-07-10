# Write a Python program using multiprocessing.Pool to calculate the
# sum of all odd numbers from 1 to N.

from multiprocessing import Pool
import os

def SumOdd(No):
    Total=0
    for i in range(1,No+1,2):
        Total+=i
    print("Process ID :",os.getpid())
    print("Input Number :",No)
    print("Sum of Odd Numbers :",Total)
    print("-"*30)
    return Total

def main():
    Data=list(map(int,input("Enter Numbers : ").split()))
    with Pool() as P:
        P.map(SumOdd,Data)

if __name__=="__main__":
    main()
