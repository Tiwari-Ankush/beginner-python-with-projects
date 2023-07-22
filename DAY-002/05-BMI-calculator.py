# BMI >> BODY MASS INDEX 
# DEFN >> WEIGHT(kg.) / HEIGHT**2 (met.sqr)

height=(input("Enter your Height in meter\n"))
weight=(input("Enter your weight in kg \n"))

BMI=(int(weight)/(float(height)**2)) # we get floating point no as a answer
BMI=int(BMI)
print("your BMI is",(round(BMI)))