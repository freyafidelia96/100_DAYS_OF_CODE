#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("C:/Users/godwi/Desktop/ores-work/PYTHON DEV/Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/example.txt", mode="r", encoding='cp1252') as file:
    content = file.read()

with open(r"C:\Users\godwi\Desktop\ores-work\PYTHON DEV\Day24\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt", mode="r", encoding='cp1252') as file:
    names_content = file.read()

names_content_list = list(names_content.split("\n"))

for name in names_content_list:
    new_content = content.replace("Aang", name)
    with open(f"Letter to {name}.txt", mode="w") as file:
        file.write(new_content)



