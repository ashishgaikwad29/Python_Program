#   Write a program which accepts one character and checks whether it is vowel or consonant.
#   Input: a 
#   Output: Vowel

def Check(Ch):
    if Ch in "aeiou":
        print("Vowel")
    else:
        print("consonant")

def main():
    Value = input("Enter a Character : ").lower()

    Check(Value)

if __name__ == "__main__":
    main()