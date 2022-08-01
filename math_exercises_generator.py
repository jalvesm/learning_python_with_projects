import random
# Values randomly generated between and 1 and 100

def generates_addition_exercise():
    term_1 = random.randrange(0,101)
    term_2 = random.randrange(0,101)
    print("{:7d}".format(term_1))
    print("+{:6d}".format(term_2))
    print("-------")
    result_of_sum = term_1 + term_2
    # print("{:7d}".format(result_of_sum))
    print("\n")

def generates_subtraction_exercise():
    minuend = random.randrange(0,101)
    subtrahend = random.randrange(0,101)
    print("{:7d}".format(minuend))
    print("-{:6d}".format(subtrahend))
    print("-------")
    result_of_subtraction = minuend - subtrahend
    # print("{:7d}".format(result_of_subtraction))
    print("\n")
        
def generates_multiplication_exercise():
    multiplier = random.randrange(0,101)
    multiplicand = random.randrange(0,101)
    product = multiplier * multiplicand
    print("{:7d}".format(multiplier))
    print("x{:6d}".format(multiplicand))
    print("-------")
    # print("{:7d}".format(product))
    print("\n\n")
    
def generates_division_exercise():
    numerator = random.randrange(0,101)
    denominator = random.randrange(1,101) 
    quotient = numerator / denominator
    # print("Aswer: {:.2f}".format(quotient))
    print("{} / {}".format(numerator, denominator))
    print("\n\n")

def showing_addition():
    print("\n1)ADDITION:")
    num_of_exercises = int(input("How many exercises do you need to practice? "))
    for addition_exercises in range(1, num_of_exercises + 1):
        generates_addition_exercise()
    
def showing_subtraction():
    print("\n2). SUBTRACTION:")
    num_of_exercises = int(input("How many exercises do you need to practice? "))
    for subtraction_exercises in range(1, num_of_exercises + 1):
        generates_subtraction_exercise()
    
def showing_multiplication():
    print("\n3) MULTIPLICATION:")
    num_of_exercises = int(input("How many exercises do you need to practice? "))
    for addition_exercises in range(1, num_of_exercises + 1):
        generates_multiplication_exercise()
    
def showing_division():
    print("\n4) DIVISION:")
    num_of_exercises = int(input("How many exercises do you need to practice? "))
    for subtraction_exercises in range(1, num_of_exercises + 1):
        generates_division_exercise()    

print("----------------------------------")
print("MATHEMATICS EXERCISES GENERATOR")
print("----------------------------------\n\n")

print("Which arithmetic operation do you wish to practice?")
print("(1) Addition")
print("(2) Subtraction")
print("(3) Multiplication")
print("(4) Division")
choice = int(input("Your choice: "))

if (choice == 1):
    showing_addition()
elif (choice == 2):
    showing_subtraction()
elif (choice == 3):
    showing_multiplication()
else:
    showing_division()

    
    # ...to be improved!
