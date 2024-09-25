import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

running = True

def stillplaying():
    still_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if still_playing == 'y':
        os.system('cls')
        blackjack()

def blackjack():
    print(logo)
    computer = random.choices(cards, k = 2)
    user = random.choices(cards, k = 2)

    running = True

    while running == True:
        print(f"\tYours cards: {user}, current score: {sum(user)}\n\tComputer's first card: {computer[0]}")

        if sum(computer) == 21:
            print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}")
            print(f"You lose with Blackjack \N{expressionless face}")
            stillplaying()


        if sum(user) == 21:
            print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}")
            print(f"You win with Blackjack \N{grinning face}")
            stillplaying()

        should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if should_continue == 'n':
            while sum(computer) <= 16:
                new_card_computer = random.choice(cards)
                if new_card_computer == 11:
                    if (sum(computer) + new_card_computer) > 21:
                        new_card_computer = 1
            
                computer.append(new_card_computer)

            print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}")
            if sum(user) > sum(computer):
                print(f"You win \N{grinning face}")
            elif sum(computer) > 21:
                print(f"Opponent went over \N{grinning face}")
            elif sum(user) == sum(computer):
                print(f"Draw \N{expressionless face}")
            else:
                print(f"You lose \N{expressionless face}")

            stillplaying()
            running = False
        else:
            new_card_user = random.choice(cards)
            new_card_computer = random.choice(cards)

            if new_card_user == 11:
                if (sum(user) + new_card_user) > 21:
                    new_card_user = 1

            user.append(new_card_user)

            if sum(user) > 21:
                print(f"\tYour final hand: {user}, final score: {sum(user)}\n\tComputer's final hand: {computer}, final score: {sum(computer)}")
                print("You went over. You lose \N{crying face}")
                stillplaying()
                break
            
            if new_card_computer == 11:
                if (sum(computer) + new_card_computer) > 21:
                    new_card_computer = 1
            
            computer.append(new_card_computer)


stillplaying()
