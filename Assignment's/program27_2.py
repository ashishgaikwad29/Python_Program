# 2: Write a Python program to implement a class named BankAccount with the following
# requirements:
# • The class should contain two instance variables:
#   ◦ Name (Account holder name)
#   ◦ Amount (Account balance)
# • The class should contain one class variable:
#   ◦ ROI (Rate of Interest), initialized to 10.5
# • Define a constructor (__init__) that accepts Name and initial Amount.
# • Implement the following instance methods:
#   ◦ Display() – displays account holder name and current balance
#   ◦ Deposit() – accepts an amount from the user and adds it to balance
#   ◦ Withdraw() – accepts an amount from the user and subtracts it from balance
#     (Ensure withdrawal is allowed only if sufficient balance exists)
#   ◦ CalculateInterest() – calculates and returns interest using formula:
#     Interest = (Amount * ROI) / 100
# • Create multiple objects and demonstrate all methods.

class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Balance :", self.Amount)

    def Deposit(self, Value):
        self.Amount += Value

    def Withdraw(self, Value):
        if Value <= self.Amount:
            self.Amount -= Value
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100


def main():

    Obj1 = BankAccount("Ashish",10000)

    Obj1.Display()

    Obj1.Deposit(5000)
    Obj1.Display()

    Obj1.Withdraw(3000)
    Obj1.Display()

    print("Interest :",Obj1.CalculateInterest())


if __name__ == "__main__":
    main()