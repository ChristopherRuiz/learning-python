# Import the random module to be able to create a (pseudo) random number.
import random

number = random.randint(1,5)                               # Generate random number
guess = 0

while int(guess) != number:
    print('Guess a number between 1 and 5: ')              # Tell user to guess number
    guess = input()                                         # Produce the user input field
    guess = int(guess)                                      # Convert guess to integer

    if guess == number:                                     # Break while loop if guess is correct
        break
    elif guess not in range(number):
        print("=====")
        print("Your guess was outside of the range. Try again!")                # This is wrong!!! fix its checking if number is greater than random number generated not end range number
        print("=====")
    else: 
        print("=====")                                      
        print('You did not guess the number! Try again.')                           # Tell user to try again 
        print("=====")                       


# Message to display when guessed
print("You guessed it! The number was: " + str(number))

###TODO
# guess counter and numbers guessed
