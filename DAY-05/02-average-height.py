
# AVERAGE HEIGHT EXERCISE- INTERACTIVE CODING EXERCISE 

students=input("Enter the No. of students\n")
students=int(students)
height=[] # list of heights 
for i in range (1,students+1):
    height_input=int(input(f" Enter the height of Student {i}:\n "))
    height.append(height_input)


print(f"\nList of height is : {height}\n")

# average
height_count=0
for a in height:
    height_count=height_count+a
# print(height_count)

height_count=float(height_count)

average = (height_count/students)
print(f"Average height is : {round(average)}\n")