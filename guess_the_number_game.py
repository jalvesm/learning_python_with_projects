

print("**********************************")
print("\tTHE GUESSING GAME")
print("**********************************")

number = 42     #Answer to the Ultimate Question of Life :)
total_of_attempts = 3
round = 1       #starts at round 1
user_guess = 0

while (round <= total_of_attempts):
    print("\n\nAttempt {} out of {}".format(round, total_of_attempts))
    user_guess_str = input("Inform your guess: ")
    user_guess = int(user_guess_str)

    guess_was_smaller = number > user_guess
    guess_was_equal = number == user_guess
    guess_was_bigger = number < user_guess

    if (guess_was_equal):
        print("YEAH, congrats! Right on the spot!\n")
    else:
        if (guess_was_smaller):
            print("Ohhh, not this time. Your guess was smaller than the actual number!")
        elif (guess_was_bigger):
            print("Ohhh, not this time. Your guess was bigger than the actual number!")
    
    round = round + 1

print("End of game!")
