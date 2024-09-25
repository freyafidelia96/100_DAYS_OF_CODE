"""import random
names_string = input("What are the names? Let's select who's to pay (chuckles)\n")


names = names_string.split(",")

who_is_to_pay = random.randint(0, len(names)-1)

print(f"\n{names[who_is_to_pay]} is to pay!")"""

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? it can be block A or B or C then you have to choose the place it can be 1 0r 2 0r 3\n").upper()

abc = ['a', 'b', 'c']

letter = position[0].lower()

letter_index = abc.index(letter)

map_first_index = int(position[1]) - 1

map[map_first_index][letter_index] = "X"




print(f"{line1}\n{line2}\n{line3}")