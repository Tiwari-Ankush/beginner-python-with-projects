# print vs return ??


def add(a,b):
    return a+b
def subscract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations ={
    "+":add,
    "-":subscract,
    "*":multiply,
    "/":divide
}

def funct_add (index_value):
    operations[index_value-1]
    
if __name__=="__main__":
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    
    print(f"operators are: ",end="")
    for key in operations:
        print(key, end=" ")
    
    operation=input("\nChoose the operator :  ")
    calculation_func=operations[operation]

    first_answer=calculation_func(num1,num2)
    print(f"{num1} {operation} {num2} = {first_answer}")



# xtra part >>>
    another_opn=input("Enter another operation: ")
    num3=int(input("Enter the Next number: "))
    calculation_func=operations[another_opn]

    second_answer=calculation_func(first_answer,num3)
    print(f"{first_answer} {another_opn} {num3} = {second_answer}")

