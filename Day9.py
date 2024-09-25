import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
go_again = True
bid_dict = {}


while go_again == True:
    name = input("What is your name? ")

    bid_price = input("What is your bid? $")
    bid_dict[name] = int(bid_price)
    repeat = input("Is there any other Bidder? yes or no: ").lower()
    if repeat == "no":
        go_again = False
    else:
        os.system('cls')

def highest_bidder(bid_dict):
    keY = ""
    max = 0
    for key, value in bid_dict.items():
        if value > max:
            max = value
            keY = key

    print(f"The highest bidder is {key} with bid ${max}")

highest_bidder(bid_dict)
