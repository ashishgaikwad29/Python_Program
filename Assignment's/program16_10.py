#   Write a program which accept name from user and display length of its name. 
#   Input : Marvellous   
#   Output : 10

def main():
    Value = str(input("Enter Name to check : "))  
    
    Ret = len(Value)

    print(Ret)      

if __name__ == "__main__":
    main()