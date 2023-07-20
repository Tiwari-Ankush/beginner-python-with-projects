# love calculator by scientific method- given by BUZZFEED
#DIFFICULT CHALLENGE
# we need here lower case characters so we use lower() function
# and also use of count( function) for counting the occurence of letters
tera_naam=input("aapka shubh naam batao\n")
uska_naam=input("uska naam batao\n")
tera_naam_upd=tera_naam.lower()
uska_naam_upd=uska_naam.lower()
print(f"tera naam {tera_naam_upd} haii ")
print(f"uska naam {uska_naam_upd} haii ")
combine=tera_naam_upd+uska_naam_upd
t=combine.count("t")
r=combine.count("r")
u=combine.count("u")
e=combine.count("e")
l=combine.count("l")
o=combine.count("o")
v=combine.count("v")
e=combine.count("e")
true=t+r+u+e
love=l+o+v+e
score=str(true)+str(love)
print(f"love score is {score}")
score=int(score)
# now interpretation >>
if score<=10 or score>=90:
    print(f"love score hai {score}, bawal cheej ho jayegi, like coke and mentos 🤣🤣🤣")
elif score>=40 and score<=50:
    print(f"love score hai {score}, kar le bhaai shaadi, kahi vo bhaag na jaaye!❤️🙌")
elif score>=51 and score<=70:
    print(f"love score hai {score}, theek hai, but ekk baar kundli dekh liyo!!")
else:
    print(f"bhaii tu to rehne hi de, sacchi batau to tu aise hi theek hai!🥲 ")