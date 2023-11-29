"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():

    # welcome
    print('Hi there! Welcome to the number guessing game')
    # set random number between 1-50
    random_num = random.randrange(1,50)
    # count number of guesses
    counter = 0
    # so long as there isn't a break, keep running the function
    while True:
      try:
        # user guess
        guess = int(input('Guess a number from 1 - 50: '))  
        if guess <= 0 or guess >= 50:
          raise Exception(f"{guess} is not between 1 - 50. Please try again.")
        
        if guess > random_num:
          print("It's lower.")
          counter +=1
        elif guess < random_num:
          print("It's higher.")
          counter +=1
        elif guess == random_num:
          counter +=1
          print(f'''You got it! The random number is {random_num}. It took you {counter} guesses.
          The game is now over.''')
          break
      except ValueError:
        print('That is not a integar. Please try again.')
      except Exception as e:
        print(e)


start_game()
