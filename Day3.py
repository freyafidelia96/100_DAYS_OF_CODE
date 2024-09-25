print("The love calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name_joined = (name1 + name2).lower()
noOf_T = name_joined.count("t")
noOf_R = name_joined.count("r") 
noOf_U = name_joined.count("u")
noOf_E = name_joined.count("e")

total1 = noOf_E + noOf_R + noOf_U + noOf_T

"""print(f"T occurs {noOf_T} time(s)")
print(f"R occurs {noOf_R} time(s)")
print(f"U occurs {noOf_U} time(s)")
print(f"E occurs {noOf_E} time(s)")

print(f"Total = {total1}")
"""
noOf_L = name_joined.count("l")
noOf_O = name_joined.count("o")
noOf_V = name_joined.count("v")

total2 = noOf_E + noOf_O + noOf_V + noOf_L 

"""print(f"L occurs {noOf_L} time(s)")
print(f"O occurs {noOf_O} time(s)")
print(f"V occurs {noOf_V} time(s)")
print(f"E occurs {noOf_E} time(s)")

print(f"Total = {total2}")
"""
love_score = int(str(total1) + str(total2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}") 