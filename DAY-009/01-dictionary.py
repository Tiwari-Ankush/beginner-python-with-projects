
# PYTHON DICTIONAROES 
# ITS A BASICALLY KEY VALUE PAIR 
# eg. >> 
# key ="bug"
# value=" an error in a program that prevents the program from running as expected"

# {key: value}

dictionary={
    "bug":"an error in a program that prevents the program from running as expected",
    "a":"A",
    "b":"B",
    "c":"C",
    200:"two hundred"
    }
print(dictionary,"\n")

print(dictionary["bug"])
print(dictionary[200])

# adding new key with their value in dictionary
dictionary["100"]="hundred"
print(dictionary,"\n")
# dictionary.clear()
print(dictionary.keys())
print(dictionary)

# proper way of printing the dictionary>>
for key in dictionary:
    print(f"{key} = {dictionary[key]}")
