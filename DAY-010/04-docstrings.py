# WHAAT IS DOCSTRINGS ACTUALLY??

def format_name(f_name,l_name):
    """This is the documentation section of a function , called a docstring..
    """
    if f_name=="" or l_name=="":
        return "please provide a valid input."
    formatted_fname=(f_name.title())
    formatted_lname=(l_name.title())
    return f"{formatted_fname} {formatted_lname}"

format_name("akush","twari")