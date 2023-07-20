# pizza delivary project
print("Welcome to the Tiwari's Pizza Store")
confirm=input("Do you want to order pizza ?\n Type (Y/N)\n")

# if size=="s" or "S":
#     total=total+90

if(confirm=="Y" or confirm=="y" or confirm=="yes"):
    size=input(f"Enter the size of  pizza \n S=small, M=medium, L=large\n")
    pepperoni=input(f"Do you want peperoni? (y/n)")
    extra_cheese=input("Do you want extra cheese? (y/n)")
    
    total=0
    if(size=="s"):
        total=total+90
    elif(size=="m"):
        total=total+150
    elif(size=="l"):
        total=total+200
    else:
        print(f"Invalid size, please enter correct !")
    
    if pepperoni=="y":
        if size=="s":
            total+=10
        elif size=="m":
            total+=20
        else:
            total+=30
    elif pepperoni=='n':
        total
    else:
        print("invalid input")

    if extra_cheese == 'y':
        if size=="s":
            total+=5
        elif size=="m":
            total+=10
        else:
            total+=15
    elif extra_cheese=='n':
        total
    else:
        print("invalid input")

    print(total)

else:
    print("Invalid input! Thanks for confirming, Have a nice day!!")




    # size=input(f"Enter the size of  pizza \n S=small, M=medium, L=large\n")




    # no_of_pizza=int(input("Enter the number of pizza you want to order\n"))

    # s_count=0
    # m_count=0
    # l_count=0
    # for i in range(1,no_of_pizza+1):
    #     size=input(f"Enter the size of {i} pizza \n S=small, M=medium, L=large\n")
    #     if(size=="s" or "S" or "small"):
    #         s_count+=1
    #     elif(size=="m" or "M" or "medium"):
    #         m_count+=1
    #     elif(size=="L" or "l" or "large"):
    #         l_count+=1
    #     else:
    #         print(f"Invalid size, please enter correct !")
    # print(s_count)
    # print(m_count)
    # print(l_count)