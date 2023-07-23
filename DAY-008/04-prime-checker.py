#  PRIME NUMBER CHECKER

n=int(input("Enter the number bro >>\n"))

def prime_checker(number):
    prime=True
    for i in range (2,(number-1)):
        if number%i ==0 :
            prime=False
    if prime:
        print(f"{n} is a Prime number\n")
    else:
        print(f"{n} is Not a Prime number\n")

if n in range(0,9999):
    if n == 0:
        print("0 is Neither Prime nor Composite number\n")
    else:    
        prime_checker(n)
else:
    print("invalid number\n")
    exit
