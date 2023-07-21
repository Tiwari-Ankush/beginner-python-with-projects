
# Additon of even numbers from a given specific range
m=int(input("Enter the starting number:\n"))
n=int(input("Enter the ending number:\n"))

evens=[]
# adding even numbers from 1 to 100
# for i in range (1,101):

# we can also use >>
# for i in range (m,n+1,2): # 2 for difference

for i in range (m,n+1):
    if i%2==0:
        evens.append(i)
    else:
        continue
# print(evens)
even_sum=0
for i in range(len(evens)):
    even_sum=even_sum+i
print(f"Sum of all Even numbers betn the range is : {even_sum}\n")
