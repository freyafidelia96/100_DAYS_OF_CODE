"""# Write your code below this line 👇
def paint_calc(height, width, cover):
  number_cans = round((height * width) / cover)
  print(f"You'll need {number_cans} cans of paint")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
"""
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(text = '', shift = 0, direction = ''):
    
    restart = True
    while restart == True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        final_text = ''
        index = 0
        for letter in text:
            if letter not in alphabet:
                final_text += letter
                continue
            position = alphabet.index(letter)
            if direction == "encode":
                index = (position + shift ) % 26
            elif direction == "decode":
                index = (position - shift) % 26
            else:
                print("Invalid input.")
            final_text += alphabet[index]
        print(f"The encoded text is {final_text}")

        repeat = input("Type 'yes' if you want to go again. Otherwise Type 'no'")
        if repeat == 'no':
           restart = False
           print("Goodbye.")
    
caesar()
    