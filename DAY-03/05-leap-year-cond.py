'''
In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
'''
year = int(input("Enter the year\n"))
if (year%4==0):
    if(year%100==0):
        if(year%400==0):    
            print(f"{year} is a Leap year\n")
        else:
            print(f"{year} is Not a Leap year\n")
    else:
        print(f"{year} is Not a Leap year\n")
else:
    print(f"{year} is Not a Leap year\n")
    
                
