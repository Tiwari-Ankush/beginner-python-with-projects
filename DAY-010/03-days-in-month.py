


def is_leap(year):
    if (year%4==0):
        if(year%100==0):
            if(year%400==0):    
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,30,31,30,31,30,31]
    month_names=["january","february","march","april","may","june","july","august","september","october","november","december"]
    if month>12 or month <1:
        return "Invalid Month entered."                
    if is_leap(year) and month ==2:
        return f"Month : {(month_names[month-1]).title()} Days: {29}"
    else:
        return f"Month : {(month_names[month-1]).title()} \nDays : {month_days[month-1]}"

if __name__=="__main__":
    year  = int(input("Enter the year: "))
    month=int(input("Enter a month number: "))
    days=days_in_month(year,month)
    print(days)