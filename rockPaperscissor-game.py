# Rock Paper Scissors ASCII Art

# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, scissors, scissors]
import random
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print("computer choose:")
print(game_images[computer_choice])
if computer_choice < 0 or user_choice >= 3:
  print("You typed the invalid number.You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You WIN!")
elif user_choice == computer_choice:
  print("It's a draw")
elif user_choice == 1 and computer_choice == 0:
    print("You WIN!")
elif user_choice == 2 and computer_choice == 0:
      print("You LOSE!")
elif computer_choice > user_choice:
  print("You LOSE!")
elif user_choice > computer_choice:
  print("You WIN!")
