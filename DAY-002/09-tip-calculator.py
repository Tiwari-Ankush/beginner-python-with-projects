# day 2 project 2 
# tip calculator >>

print("Welcome to the tip calculator by Ankush.")

total_bill=input("What was the total bill in INR?\n")
total_bill=float(total_bill)
print(f"Total bill is INR {total_bill}\n")

tip=input("What percentage tip would you like to give?\n")
tip=int(tip)
print(f"Tip is {tip} %\n")

people=input("How many people to split the bill?\n")
people=int(people)
print(f"Number of peoples are {people}\n")

tip_total_amt=(total_bill*tip/100)
print(f"Total tip amount is INR {tip_total_amt}\n")

final_amt=total_bill+tip_total_amt
final_amt=float(final_amt)
final_amt=round(final_amt,2)
print(f"Final amount including tip amoount is INR {final_amt}\n")

each_person=(final_amt/people)
each_person=round(each_person,2)

print(f"Each person should pay: INR {each_person}")

