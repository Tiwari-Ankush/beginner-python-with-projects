'''
program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill
'''
# not allowed to use a choice() function

import random
# take string as a input
# using str.split(' , ')

print('''

W H O - P A Y S - T H E - W H O L E - B I L L
''')

# friends=["ankush","john","salman","chaitanya","angela","jordan","cristopher","robert","peter","harrypotter"]
# STATICALLY >>
friends="ankush,john,salman,chaitanya,angela,jordan,christopher,robert,peter,harrypotter"

# DYNAMICALLY >>
# friends=input("Enter the names of your friends in comma separed format :\n")
lst=friends.split(",")  # IT COVERT STRING TO LIST
# print(lst)


bill_payer=random.randint(0,(len(lst)-1))
# print(bill_payer)
print(f"SO THE BILL WILL PAY BY >>> {lst[bill_payer]}\n")


# bill_payer=random.choice(lst) #using choice() function 
# print(bill_payer)
