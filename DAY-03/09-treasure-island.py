# https://ascii.co.uk/art #website
print("welcome to the treasure island project by Ankush")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
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
        print("\n now it is a last stage of treasure\nThere are 3 doors red, blue, and yellow door\n")

        door=input("Choose one door to reach the treasure.\ntype (red / yellow / blue)\n")

        if door=="red" or door=="blue":
            print("Sorry, you loss the treasure, game-over.")
        elif door=="yellow":
            print("Great, You won the game and Found the treasure 😍😍😍")
        else:
            print("invalid input")

    else:
        print("invalid input")

else:
    print("invalid input")