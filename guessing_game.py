"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random



def start_game():
    high_score = 1009
    # welcome
    print(f'Hi there! Welcome to the number guessing game.')
    if high_score != 1000:
      print(f'The high score is {high_score}')
    # set random number between 1-50
    random_num = random.randrange(1,50)
    # count number of guesses
    counter = 0
    # so long as there isn't a break, keep running the function
    while True:
      try:

        # user guess
        guess = int(input('Guess a number from 1 - 50: '))
        
        # check if input is in the range
        if guess <= 0 or guess >= 50:
          raise Exception(f"{guess} is not between 1 - 50. Please try again.")
        
        # give clues
        if guess > random_num:
          print("It's lower.")
          counter +=1
        elif guess < random_num:
          print("It's higher.")
          counter +=1
          
        # wins game
        elif guess == random_num:
          counter +=1
          print(f'''You got it! The random number is {random_num}. It took you {counter} guesses.
          The game is now over.''')
          
          # check high score
          if counter < high_score:
            high_score = counter
            print(f'---- NEW HIGH SCORE! ---- << {high_score} >> ')
            
          # play again?  
          again = input("Would you like to play again? ")
          if again == 'no':  
            break
          
          # reset the game
          else:
            counter = 0
            random_num = random.randrange(1,50)
            
      # handle errors      
      except ValueError:
        print('That is not a integar. Please try again.')
      except Exception as e:
        print(e)


start_game()
