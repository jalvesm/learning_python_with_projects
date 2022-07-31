import random

print("**********************************")
print("\tTHE GUESSING GAME")
print("**********************************")

secret_number = random.randrange(1,101)

print("Selec the level of difficulty:")
print("(1) Easy\t (2) Medium\t (3) Hard")
user_choice = int(input("Your choice: "))

if (user_choice == 1):
    total_of_attempts = 25
elif (user_choice == 2):
    total_of_attempts = 15
else:
    total_of_attempts = 5
    
    
for round in range (1, total_of_attempts + 1):
    print("\n\nAttempt {} out of {}".format(round, total_of_attempts))
    user_guess = int(input("Inform your guess: "))

    guess_was_smaller = secret_number > user_guess
    guess_was_equal = secret_number == user_guess
    guess_was_bigger = secret_number < user_guess

    if (guess_was_equal):
        print("YEAH, congrats! Right on the spot!\n")
        break
    else:
        if (guess_was_smaller):
            print("Ohhh, not this time. Your guess was smaller than the actual number!")
        elif (guess_was_bigger):
            print("Ohhh, not this time. Your guess was bigger than the actual number!")

print("End of game!")
