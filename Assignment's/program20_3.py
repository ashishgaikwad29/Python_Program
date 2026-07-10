# Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should extract all even elements from the list,
# calculate and display their sum.
# The OddList thread should extract all odd elements from the list,
# calculate and display their sum.
# Threads should run concurrently.

import threading

def EvenList(Data):
    Sum = 0
    print("Even Elements :", end=" ")
    for i in Data:
        if i % 2 == 0:
            print(i, end=" ")
            Sum += i
    print("\nSum of Even Elements :", Sum)

def OddList(Data):
    Sum = 0
    print("Odd Elements  :", end=" ")
    for i in Data:
        if i % 2 != 0:
            print(i, end=" ")
            Sum += i
    print("\nSum of Odd Elements :", Sum)

def main():
    Size = int(input("Enter Number of Elements : "))
    Data = list(map(int, input("Enter Numbers : ").split()))

    T1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    T2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
