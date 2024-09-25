import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_list = [rock, paper, scissors]

choice = int(input("What do want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

computer_choice = random.randint(0, 2)

if choice == 0 and computer_choice == 1:
    print(f"{choices_list[choice]}\nComputer chose {computer_choice}\n{choices_list[computer_choice]}\nIt's a draw.")
elif choice == 1 and computer_choice == 2:
    print(f"{choices_list[choice]}\nComputer chose {computer_choice}\n{choices_list[computer_choice]}\nIt's a draw.")
elif choice == 2 and computer_choice == 0:
    print(f"{choices_list[choice]}\nComputer chose {computer_choice}\n{choices_list[computer_choice]}\nIt's a draw.")
elif choice == computer_choice:
    print(f"{choices_list[choice]}\nComputer chose {computer_choice}\n{choices_list[computer_choice]}\nIt's a draw.")
elif choice > 2 or choice < 0:
    print("Invalid input.")
else:
    print(f"{choices_list[choice]}\nComputer chose {computer_choice}\n{choices_list[computer_choice]}\nIt's a draw.")

