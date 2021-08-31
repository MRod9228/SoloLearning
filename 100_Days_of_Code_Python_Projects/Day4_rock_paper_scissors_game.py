import random
import time

def rock_paper_scissors_game():
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


    game_images = [rock, paper, scissors]
    user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
    if user_choice >= 3 or user_choice < 0:
        print('Invalid selection, you lose!')
    else: 
        print('You choose' + game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print('The computer choose:')
        print(game_images[computer_choice])


        if user_choice == 0 and computer_choice == 2:
            print('You win!')
        elif user_choice == 2 and computer_choice == 0:
            print('You win!')
        elif user_choice < computer_choice:
            print('You lose.')
        elif user_choice > computer_choice:
            print('You win!')
        elif user_choice == computer_choice:
            print('Is a draw!')
        else:
            print('This should never show up')


print(rock_paper_scissors_game())
time.sleep(5)
