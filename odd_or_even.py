# write an algorithm to read two values from keyboard and tell if the first value is even and positive, and the second value is odd and negative

def check_remainder(value):
    even = (value % 2) == 0
    
    if (even):
        print("The number {} is even.".format(value))
    else:
        print("The number {} is odd.".format(value))

def check_signal(value):
    positive = value > 0
    
    if (positive):
        print("The number {} is positive.".format(value))
    else:
        print("The number {} is negative.".format(value))


first_value = int(input("Insert the first value: "))
second_value = int(input("Insert the second value: "))

check_remainder(first_value)
check_signal(first_value)
print()
check_remainder(second_value)
check_signal(second_value)
