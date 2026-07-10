# Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def Maximum(Data):
    print("Maximum Element :", max(Data))

def Minimum(Data):
    print("Minimum Element :", min(Data))

def main():
    Size=int(input("Enter Number of Elements : "))
    Data=list(map(int,input("Enter Numbers : ").split()))
    T1=threading.Thread(target=Maximum,args=(Data,),name="Maximum")
    T2=threading.Thread(target=Minimum,args=(Data,),name="Minimum")
    T1.start(); T2.start()
    T1.join(); T2.join()

if __name__=="__main__":
    main()
