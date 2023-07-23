# create a function caalled greet 
# write 3 print functions inside that function

# def function(variable):
    # do this with @variable
    # pass
# function("variable value")

def greet(name):
    print(f"hello {name}")
    print(f"how are you? {name}")
    print(f"are you fine? {name}")

username=input("Enter your name >> \n")
greet(username)