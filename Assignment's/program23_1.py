# Write a Python program using multiprocessing.Pool to calculate the
# sum of all even numbers from 1 to N for every number from the given list.

from multiprocessing import Pool
import os

def SumEven(No):
    Total=0
    for i in range(2,No+1,2):
        Total+=i
    print("Process ID :",os.getpid())
    print("Input Number :",No)
    print("Sum of Even Numbers :",Total)
    print("-"*30)
    return Total

def main():
    Data=list(map(int,input("Enter Numbers : ").split()))
    with Pool() as P:
        P.map(SumEven,Data)

if __name__=="__main__":
    main()
