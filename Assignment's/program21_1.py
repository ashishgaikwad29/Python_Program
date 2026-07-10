# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading

def CheckPrime(No):
    if No < 2:
        return False
    for i in range(2,int(No**0.5)+1):
        if No % i == 0:
            return False
    return True

def Prime(Data):
    print("Prime Numbers :", end=" ")
    for i in Data:
        if CheckPrime(i):
            print(i,end=" ")
    print()

def NonPrime(Data):
    print("Non Prime Numbers :", end=" ")
    for i in Data:
        if not CheckPrime(i):
            print(i,end=" ")
    print()

def main():
    Size=int(input("Enter Number of Elements : "))
    Data=list(map(int,input("Enter Numbers : ").split()))
    T1=threading.Thread(target=Prime,args=(Data,),name="Prime")
    T2=threading.Thread(target=NonPrime,args=(Data,),name="NonPrime")
    T1.start(); T2.start()
    T1.join(); T2.join()

if __name__=="__main__":
    main()
