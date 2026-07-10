# Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
# Thread ID
# Thread Name

import threading

def Small(Str):
    Count = sum(1 for ch in Str if ch.islower())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small Characters :", Count)

def Capital(Str):
    Count = sum(1 for ch in Str if ch.isupper())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital Characters :", Count)

def Digits(Str):
    Count = sum(1 for ch in Str if ch.isdigit())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", Count)

def main():
    Value = input("Enter String : ")

    T1 = threading.Thread(target=Small, args=(Value,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()
