#   Write a program which accepts radius of circle and prints area of circle.

def Area(radius):
    Ans = 3.14 * radius * radius
    return Ans

def main():
    Value = int(input("Enter Number : "))    

    Ret = Area(Value)

    print("Area is : ",Ret)    

if __name__ == "__main__":
    main()