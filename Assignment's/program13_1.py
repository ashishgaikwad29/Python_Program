#    Write a program which accepts length and width of rectangle and prints area.

def Area(Length, Width):
    return Length * Width

def main():
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))        

    Ret = Area(Value1, Value2)

    print("Area is : ",Ret)

if __name__ == "__main__":
    main()