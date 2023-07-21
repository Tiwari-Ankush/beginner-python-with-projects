print('''

  F I Z Z  B U Z Z  G A M E  
B Y  A N K U S H  T I W A R I
 
''')

for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num %3==0:
        print("Fizz")
    elif num %5==0:
        print("Buzz")
    else:
        print(num)
