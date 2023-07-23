
# positional arguments >> position is passed as an argument while calling a function
def greet(name):
    print(f"hello {name}")
    print(f"how are you? {name}")
    print(f"are you fine? {name}\n")

username=input("Enter your name >> \n")
greet(username)

# keyword arguments >> directly value is passed with = sign to the function arguments
def greet(name="tiwari", surname="ankush", nickname ="none"):
    print(f"hello {name}  {surname} {nickname}")
    print(f"how are you? {name} {surname} {nickname}")
    print(f"are you fine? {name} {surname} {nickname}")
greet()