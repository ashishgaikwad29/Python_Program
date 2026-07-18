# 3: Write a Python program to implement a class named Numbers with the following
# specifications:
# • The class should contain one instance variable:
#   ◦ Value
# • Define a constructor (__init__) that accepts a number from the user and initializes Value.
# • Implement the following instance methods:
#   ◦ ChkPrime() – returns True if the number is prime, otherwise returns False
#   ◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
#   ◦ Factors() – displays all factors of the number
#   ◦ SumFactors() – returns the sum of all factors
# • Create multiple objects and call all methods.

class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):

        Count = 0

        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                Count += 1

        if Count == 2:
            return True
        else:
            return False

    def Factors(self):

        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(i,end=" ")

        print()

    def SumFactors(self):

        Sum = 0

        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Sum += i

        return Sum

    def ChkPerfect(self):

        if(self.SumFactors() == self.Value):
            return True
        else:
            return False

def main():

    No = int(input("Enter number : "))

    Obj = Numbers(No)

    Obj.Factors()

    print("Sum of factors :",Obj.SumFactors())

    if Obj.ChkPrime():
        print("Prime Number")
    else:
        print("Not Prime Number")

    if Obj.ChkPerfect():
        print("Perfect Number")
    else:
        print("Not Perfect Number")

if __name__ == "__main__":
    main()