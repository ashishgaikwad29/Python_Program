#   Write a program which accept number from user and print that number of “*” on screen. 
#   Input : 5    
#   Output : * * * * * 

def main():
    Value = int(input("Enter Number of * you want to print it on screen : "))

    for i in range(Value):
        print("*", end=" ")        

if __name__ == "__main__":
    main()

###################################################################################################################################