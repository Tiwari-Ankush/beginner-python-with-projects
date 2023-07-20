# BMI >> BODY MASS INDEX 
# DEFN >> WEIGHT(kg.) / HEIGHT**2 (met.sqr)

# INTERPRETATION CONDITIONS ..>>
# UNDER 18.5 UNDERWEIGHT
# OVER 18.5 BUT BELOW 25 NORMAL weight
# OVER 25 BUT BELOW 30 OVERWEIGHT
# OVER 30 BUT BELOW 35 OBESE
# ABOVE 35 CLINICALLY OBESE

height=(input("Enter your Height in meter\n"))
weight=(input("Enter your weight in kg \n"))

BMI=(int(weight)/(float(height)**2)) # we get floating point no as a answer
BMI=int(BMI)
print("your BMI is",(round(BMI)),end=" ")

if(BMI<18.5):
    print(f"and you are UNDERWEIGHT\n")
elif(BMI<25):
    print(f"and you have NORMAL weight \n")
elif(BMI<30):
    print(f"and you are OVERWEIGHT\n")
elif(BMI<35):
    print(f"and you are OBESE\n")
else:
    print(f"and you are CLINICALLY OBESE\n")
    
