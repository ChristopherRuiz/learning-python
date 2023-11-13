# Import the random module to be able to create a (pseudo) random number.
import random

number = random.randint(1,25)                               # Generate random number
guess = 0

while int(guess) != number:
    print('Guess a number between 1 and 25: ')              # Tell user to guess number
    guess = input()                                         # Produce the user input field
    guess = int(guess)                                      # Convert guess to integer

    if guess == number:                                     # Break while loop if guess is correct
        break
    elif guess > number:
        print("=====")
        print("Number is between 1 and 25!")                # Remind user of the range
        print("=====")
    else: 
        print("=====")                                      
        print('Nope! Try again.')                           # Tell user to try again 
        print("=====")                       


# Message to display when guessed
print("You guessed it! The number was: " + str(number))

###TODO
# guess counter and numbers guessed