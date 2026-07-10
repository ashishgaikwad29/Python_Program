# Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

import threading

Counter = 0
Lock = threading.Lock()

def Increment():
    global Counter
    for i in range(100000):
        with Lock:
            Counter += 1

def main():
    T1 = threading.Thread(target=Increment)
    T2 = threading.Thread(target=Increment)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Final Counter :", Counter)

if __name__ == "__main__":
    main()
