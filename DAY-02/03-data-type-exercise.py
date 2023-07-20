# enter the two digit number
# and add them by each other 
# remember int object is not subscriptable

two_digit=input("enter the two digit no. ")
print(two_digit)
print(type(two_digit))

two_digit=str(two_digit)

add=(int(two_digit[0])+int(two_digit[1]))
print(add)