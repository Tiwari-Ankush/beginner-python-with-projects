


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

    answer=calculation_func(num1,num2)
    
    print(f"{num1} {operation} {num2} = {answer}")