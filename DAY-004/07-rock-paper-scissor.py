print("""
W E L C O M E - T O - R O C K - P A P E R - S C I S S O R
              ---------✊-🫱-🖖-----------
             B Y - A N K U S H - T I W A R I 
""")

import random # for computer

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# options = ["ROCK","PAPER","SCISSOR"]
# computer_input=random.choice(options)
# print(computer_input)

# for accessing ascii images
game=[rock,paper,scissor]

#for user
user_input=input("Enter value >>\n 0 >> ROCK\n 1 >> PAPER\n 2 >> SCISSOR\nINPUT = ")
print("\n")
user=""
if user_input in ["0","1","2"]:
    if user_input=="0":
        # print("ROCK")
        user="ROCK"
        
    elif user_input=="1":
        # print("PAPER")
        user="PAPER"
    else:
        # print("SCISSOR")
        user="SCISSOR"
    
    user_input=int(user_input)
    print(f"You : {game[user_input]}\n{user}\n")

    #  for computer
    computer_input=random.randint(0,2)
    computer_input=str(computer_input)
    computer="ksksksu"
    if computer_input in ["0","1","2"]:
        if computer_input=="0":
            # print("ROCK")
            computer="ROCK"
        
        elif computer_input=="1":
            # print("PAPER")
            computer="PAPER"
        else:
            # print("SCISSOR")
            computer="SCISSOR"
        # print(computer)
        computer_input=int(computer_input)
        print(f"Computer : {game[computer_input]}\n{computer}\n")

if user=="ROCK" and computer=="PAPER":
    print("COMPUTER WON ⭐\n")
elif user=="ROCK" and computer=="SCISSOR":
    print("YOU WON ⭐\n")
elif user=="PAPER" and computer=="ROCK":
    print("YOU WON ⭐\n")
elif user=="PAPER" and computer=="SCISSOR":
    print("COMPUTER WON ⭐\n")
elif user=="SCISSOR" and computer=="PAPER":
    print("YOU WON ⭐\n")
elif user=="SCISSOR" and computer=="ROCK":
    print("COMPUTER WON ⭐\n")
elif user=="ROCK" and computer=="ROCK":
    print("MATCH DRAW 🤷‍♂️\n ")
elif user=="PAPER" and computer=="PAPER":
    print("MATCH DRAW 🤷‍♂️\n ")
elif user=="SCISSOR" and computer=="SCISSOR":
    print("MATCH DRAW 🤷‍♂️\n ")

else:
    print(f"Invalid input {user_input}")

