from game_data import data
from art import logo, vs
import random
import os

def isPlaying():
    stillPlaying = input("Do you want to play Higher vs Lower game? Type 'y' or 'n': ").lower()
    if stillPlaying == 'y':
        os.system("cls")
        HigherLower()


def HigherLower():
    data1 = random.choice(data)

    isCorrect = True
    score = 0

    while isCorrect == True:
        data2 = random.choice(data)

        while data1 == data2:
            data2 = random.choice(data)

        followers_count1 = data1['follower_count']
        followers_count2 = data2['follower_count']

        print(logo)
        print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}")

        print(vs)
        print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        choice_dict = {'a': 0, 'b': 1}
        choice_list = [followers_count1, followers_count2]

        check1 = choice_list[choice_dict[answer]]
        check2 = choice_list[choice_dict[answer] - 1]

        checkpoint = check1 > check2

        if checkpoint:
            score += 1
            print(f"You're right! Current score: {score}")
            data1 = data2
        else:
            print(f"You're wrong \N{expressionless face}\nFinal score: {score}")
            isCorrect = False
            isPlaying()
    
isPlaying()

