

# treasure map 

print("""
W E L C O M E - T O - T R E A S U R E - M A P
---------🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁-----------
       B Y - A N K U S H - T I W A R I 
""")
row1 =["   " , "   " , "   "]
row2 =["   " , "   " , "   "]
row3 =["   " , "   " , "   "]
map= [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
# pos_list=["11","12","13","21","22","23","31","32","33"]
pos= input("where you want to put the treasure? enter number\nfirst for column and 2nd for row\n")

if pos in ["11","12","13","21","22","23","31","32","33"]:
    
        horizontal=int(pos[0])  # input taken from pos, 1st place is row so first postion digit is stored as horixintal
        vertical=int(pos[1])     # input taken from pos, 2nd place is column so second postion digit is stored as vertical
        # print(map[vertical-1])
        
        # map[vertical-1][horizontal-1] = "🎁 " #simplified view of below two loc
        selected_row= map[vertical-1]
        selected_row[horizontal-1] = "🎁 "
        
        print(f"{row1}\n{row2}\n{row3}")
        print("Treasure mapped successfully😍")
else:
        print("Treasure cant be map, invalid place😒.")   

