num=input("Enter the number\n")
num=int(num)

if(num==0):
    print(f"{num} is not Even Number nor Odd Number\n")
elif(num%2==0):
    print(f"{num} is Even Number\n")
else:
    print(f"{num} is Odd Number\n")