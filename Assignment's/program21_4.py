# Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading

SumResult = 0
ProductResult = 1

def SumList(Data):
    global SumResult
    SumResult = sum(Data)

def ProductList(Data):
    global ProductResult
    ProductResult = 1
    for i in Data:
        ProductResult *= i

def main():
    Size = int(input("Enter Number of Elements : "))
    Data = list(map(int, input("Enter Numbers : ").split()))

    T1 = threading.Thread(target=SumList, args=(Data,))
    T2 = threading.Thread(target=ProductList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum :", SumResult)
    print("Product :", ProductResult)

if __name__ == "__main__":
    main()
