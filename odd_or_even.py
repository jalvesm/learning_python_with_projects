# write an algorithm to read a value from keyboard and tell if it's positive or negative, and if it's even or odd

def checking_remainder(value):
    true = (value % 2) == 0
    return true

def checking_signal(value):
    true = value > 0
    return true

number = int(input("Type a number to test if it is even or odd, positive or negative: "))

even = checking_remainder(number)
if (even):
    print("the number {} is even".format(number))
else:
    print("the number {} is odd.".format(number))

positive = checking_signal(number)
if (positive):
    print("The number {} is positive.".format(number))
else:
    print("The number {} is negative.".format(number))

    

# i choose SUCH terrible names for these functions and variables! 
# gotta change them all this week, sorry for that :/
