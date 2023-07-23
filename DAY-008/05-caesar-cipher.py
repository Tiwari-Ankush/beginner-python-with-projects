
import caesar 

print("""
Julius Caesar :)   
""")
print(caesar.logo)


# COMBINE CODE >>
def caesor(start_text,shift_amt,cipher_direction):
    final_text=""
    if shift_amt==0:
        print(start_text)
    else:
        for letter in start_text:
            index=caesar.alphabet.index(letter)
            if cipher_direction=="encode" or direction== "Encode" or direction=="encrypt":
                shift_index=index+shift_amt
            elif cipher_direction == "decode" or direction == "Decode" or direction=="decrypt":
                shift_index=index-shift_amt
            else:
                print("Invalid Input, try again :)")
            final_text+=caesar.alphabet[shift_index]
        print(f"The {cipher_direction}d text is : {final_text}\n")

"""
def encrypt(plain_text,shift_amt):
    if shift_amt==0:
        print(plain_text)
    else:
        cipher_text=""
        for letter in plain_text:
            index=caesar.alphabet.index(letter)
            shift_index=index+shift_amt
            cipher_text+=caesar.alphabet[shift_index]
        print(f"The encoded text is: {cipher_text}")
# encrypt(text,shift)


def decrypt(cipher_text,shift_amt):
    if shift_amt==0:
        print(cipher_text)
    else:
        plain_text=""
        for letter in cipher_text:
            index=caesar.alphabet.index(letter)
            shift_index=index-shift_amt
            plain_text+=caesar.alphabet[shift_index]
        print(f"The decoded text is: {plain_text}")
# decrypt(text,shift)

"""

if __name__ =="__main__":

    #  COMBINE WAALA INPUT 
    try_again=True
    while try_again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesor(start_text=text,shift_amt=shift,cipher_direction=direction)
        result=input("Do you want to go again -- yes or no ? \n")
        if result=="no" or result=="NO":
            try_again=False
            print("Good bye :)\n")
        if result=="yes" or result=="YES":
            try_again=True
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
 
    """    
     #  SEPARATE WALA INPUT 
    try_again=True
    while try_again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        if direction=="encode" or direction== "Encode" or direction=="encrypt":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encrypt(plain_text=text,shift_amt=shift)
        
        elif direction == "decode" or direction == "Decode" or direction=="decrypt":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decrypt(cipher_text=text,shift_amt=shift)

        else:
            print("Invalid Input :)\n")

        result=input("Do you want to go again -- yes or no ? \n")
        if result=="no" or result=="NO":
            try_again=False
            print("Good bye :)\n")
        if result=="yes" or result=="YES":
            try_again=True
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    """

