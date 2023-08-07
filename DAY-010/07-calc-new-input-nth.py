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


if __name__=="__main__":
    continue_next=True
    while continue_next :   
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the next number: "))
        print(f"operators are: ",end="")
        
        for key in operations:
            print(key, end=" ")
        
        operation=input("\nChoose the operator :  ")
        calculation_func=operations[operation]

        first_answer=calculation_func(num1,num2)
        print(f"{num1} {operation} {num2} = {round(first_answer)}")
    
        confirmation=input("Do you want to continue Y or N: ")
        if confirmation=="y" or confirmation=="Y":
            continue_next=True
            
        else:
            continue_next= False
            print(f"{num1} {operation} {num2} = {round(first_answer)}")
            
