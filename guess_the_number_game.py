print("***********************************************")
welcome_message = "Hey there, welcome to this guessing game!"
print(welcome_message)
print("***********************************************")

nickname = input("Inform your nickname, please, so we can get to know each other: ")
print("Nice to meet you,", nickname, "!\nI'm Jo, the person who developed this small game :)")
print("Let's get started!")

secret_number = 42

user_guessed_str = input("\nOkay, type a number: ")
print("You've typed ", user_guessed_str)
user_guessed = int(user_guessed_str)

if (secret_number == user_guessed):
    print("YEA, you're the best!")
else:
    print("Wow, looks like we still don't have a Sherlock over here ...")

print("Thank you for making part of it! This is the end of the game :)")
