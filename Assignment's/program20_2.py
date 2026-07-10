# Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should identify all even factors of the given number,
# calculate and display the sum of even factors.
# The OddFactor thread should identify all odd factors of the given number,
# calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display:
# "Exit from main"

import threading

def EvenFactor(No):
    Sum = 0
    print("Even Factors : ", end="")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i, end=" ")
            Sum += i
    print("\nSum of Even Factors :", Sum)

def OddFactor(No):
    Sum = 0
    print("Odd Factors  : ", end="")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i, end=" ")
            Sum += i
    print("\nSum of Odd Factors :", Sum)

def main():
    Value = int(input("Enter Number : "))

    T1 = threading.Thread(target=EvenFactor, args=(Value,), name="EvenFactor")
    T2 = threading.Thread(target=OddFactor, args=(Value,), name="OddFactor")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
