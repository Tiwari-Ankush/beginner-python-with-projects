


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
    operation=input("enter the operation >> \nadd (+) or sub (-) or multiply (*) or divide (/)\n: ")
    if operation=="add":
        index=1
        funct_add(index)