# return is the end of the function 

def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "please provide a valid input."
    formatted_fname=(f_name.title())
    formatted_lname=(l_name.title())
    return f"{formatted_fname} {formatted_lname}"

print(format_name(input("What is your first name??\n"),input("What is your last name??\n")))
