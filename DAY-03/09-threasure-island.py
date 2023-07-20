# ascii.co.uk #website
print("welcome to the threasure island project by Ankush")
name=input("Provide me your name\n")
lr_input=input(f"so {name}\nfor moviing further, there are two ways left and right,\nwhich will you choose? (left or right)\n")
if lr_input=="right":
    print("Sorry, there is no way, game-over.")
elif lr_input=="left":
    print("\ngreat!!\nyou chose the right way🙌")
    action=input("now there is a wave of water\nDo you want to Swim or Wait untill wave will gone?\ntype (swim / wait)\n")
    
    if action=="swim":
        print("Sorry, there is no way, game-over.")
    elif action=="wait":
        print("\ngreat!!\nyou chose the right way🙌")
        print("\n now it is a last stage of threasure\nThere are 3 doors red, blue, and yellow door\n")

        door=input("Choose one door to reach the threasure.\ntype (red / yellow / blue)\n")

        if door=="red" or door=="blue":
            print("Sorry, you loss the threasure, game-over.")
        elif door=="yellow":
            print("Great, You won the game and Found the threasure 😍😍😍")
        else:
            print("invalid input")

    else:
        print("invalid input")

else:
    print("invalid input")