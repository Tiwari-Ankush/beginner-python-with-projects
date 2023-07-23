
#JYAADA CANS CHALEGA BUT KAMM NAHI AAANA CHAHIYE,ISLIYE USE CEIL() FUNCTION OF MATHS MODULE, NOT USE ROUND( ) FUNCTION
# 1 can of paint cover 5 sq.mtr 

import math

height=float(input("Enter the height in meter\n"))
width = float(input("Enter the width in meter\n"))
coverage=5

def paint_calculator(height_t=height,coverage_t=coverage,width_t=width):
    area=height_t*width_t
    # calculate how many cans are required >>
    cans= area/coverage_t
    print(f"No of cans required to fill the {area} sq.mtr area >> {math.ceil(cans)} cans.\n")

if __name__ == "__main__":
    calc=(height,width,coverage)
    # print(calc)
    paint_calculator()
    
    

