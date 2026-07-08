#   Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
#   for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
#   parameters as number and perform the operation. Write on python program which call all the 
#   functions from Arithmetic module by accepting the parameters from user.

import program17_1_1

def main():
    Value1 = int(input("Enter Number 1 : "))
    Value2 = int(input("Enter Number 2 : "))  

    print("Addition is       : ",program17_1_1.Add(Value1,Value2))
    print("Substraction is   : ",program17_1_1.Sub(Value1,Value2))
    print("Multiplication is : ",program17_1_1.Mult(Value1,Value2))
    print("Division is       : ",program17_1_1.Div(Value1,Value2))       

if __name__ == "__main__":
    main()