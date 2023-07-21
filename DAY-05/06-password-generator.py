print("""
     WELCOME TO THE PASSWORD GENERATOR
             BY ANKUSH TIWARI
             🔒🔒🔒🔒🔒🔒
""")

import random

letters=['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m','A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','&','(',')','*','+']

n_letters=int(input("How many letters you want in your password?\n"))
n_numbers=int(input("How many numbers you want in your password?\n"))
n_symbols=int(input("How many symbols you want in your password?\n"))

# SIMPLE CHALLENGE
password_list=[]

for i in range(0,n_letters):
    rand_letter=random.choice(letters)
    password_list.append(rand_letter)

for i in range(0,n_numbers):
    rand_number=random.choice(numbers)
    password_list.append(rand_number)

for i in range(0,n_symbols):
    rand_symbol=random.choice(symbols)
    password_list.append(rand_symbol)

# print(password_list)


# HARD CHALLENGE STARTS >> PASSWORD IN RANDOM ORDER

count=(n_letters+n_numbers+n_symbols)

random.shuffle(password_list)  # after shuffling the list it returns none

print(password_list)

password=""
for pass_char in password_list:
    password=password+pass_char

print(f"Your {count} characters Password is >> {password}")
