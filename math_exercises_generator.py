import random

print("\t ARITHMETIC EXERCISES GENERATOR\n\n")

# Values randomly generated between and 1 and 100

def generate_addition_exercise():
    term_1 = random.randrange(0,101)
    term_2 = random.randrange(0,101)
    print("{:7d}".format(term_1))
    print("+{:6d}".format(term_2))
    print("-------")
    result_of_sum = term_1 + term_2
    # print("{:7d}".format(result_of_sum))
    print("\n")

def generate_subtraction_exercise():
    minuend = random.randrange(0,101)
    subtrahend = random.randrange(0,101)
    print("{:7d}".format(minuend))
    print("-{:6d}".format(subtrahend))
    print("-------")
    result_of_subtraction = minuend - subtrahend
    # print("{:7d}".format(result_of_subtraction))
    print("\n")
        
def generate_multiplication_exercise():
    multiplier = random.randrange(0,101)
    multiplicand = random.randrange(0,101)
    product = multiplier * multiplicand
    print("{:7d}".format(multiplier))
    print("x{:6d}".format(multiplicand))
    print("-------")
    # print("{:7d}".format(product))
    print("\n\n")
    
def generate_division_exercise():
    numerator = random.randrange(0,101)
    denominator = random.randrange(1,101) 
    quotient = numerator / denominator
    # print("Aswer: {:.2f}".format(quotient))
    print("{} / {}".format(numerator, denominator))
    print("\n\n")


def generate_addition_exercise():
    term_1 = random.randrange(0,101)
    term_2 = random.randrange(0,101)
    print("{:7d}".format(term_1))
    print("+{:6d}".format(term_2))
    print("-------")
    result_of_sum = term_1 + term_2
    # print("{:7d}".format(result_of_sum))
    print("\n")

def generate_subtraction_exercise():
    minuend = random.randrange(0,101)
    subtrahend = random.randrange(0,101)
    print("{:7d}".format(minuend))
    print("-{:6d}".format(subtrahend))
    print("-------")
    result_of_subtraction = minuend - subtrahend
    # print("{:7d}".format(result_of_subtraction))
    print("\n")
        
def generate_multiplication_exercise():
    multiplier = random.randrange(0,101)
    multiplicand = random.randrange(0,101)
    product = multiplier * multiplicand
    print("{:7d}".format(multiplier))
    print("x{:6d}".format(multiplicand))
    print("-------")
    # print("{:7d}".format(product))
    print("\n\n")
    
def generate_division_exercise():
    numerator = random.randrange(0,101)
    denominator = random.randrange(1,101) 
    quotient = numerator / denominator
    # print("Aswer: {:.2f}".format(quotient))
    print("{} / {}".format(numerator, denominator))
    print("\n\n")

def display_addition(num_of_exercises):
    print("\n 1)ADDITION:\n")
    for addition_exercises in range(1, num_of_exercises + 1):
        generate_addition_exercise()
    
def display_subtraction(num_of_exercises):
    print("\n 2) SUBTRACTION:")
    for subtraction_exercises in range(1, num_of_exercises + 1):
        generate_subtraction_exercise()
    
def display_multiplication(num_of_exercises):
    print("\n 3) MULTIPLICATION:")
    for generate_multiplication_exercise in range(1, num_of_exercises + 1):
        generate_multiplication_exercise()
    
def display_division(num_of_exercises):    
    print("\n 4) DIVISION:")
    for subtraction_exercises in range(1, num_of_exercises + 1):
        generate_division_exercise() 

        
def display_all_operations():

    display_addition()
    display_subtraction()
    display_multiplication()
    display_division()


def exit_program():
    print("Exit successfully!")


def main_menu():

    print("Which arithmetic operation do you need to practice?")
    print("\t 1) Addition")
    print("\t 2) Subtraction")
    print("\t 3) Multiplication")
    print("\t 4) Division")
    print("\t 5) Practice all of them")
    print("\t 6) Exit program")
    choice = int(input("\t\tYou choose: "))

    if (choice == 1):
        display_addition()      #pahaps "execute_addition" is a proper variable name!
    
    elif (choice == 2):
        display_subtraction()
    
    elif (choice == 3):
        display_multiplication()
    
    elif (choice == 4):
        display_division()
    
    elif (choice == 5):
        display_all_operations()
    
    elif (choice == 6):
        exit_program()
    
    else:
        print(" Oops, '{}' isn't defined. Try again!".format(choice))
        main_menu()

        
def request_input_exercices():  # menu_how_much_exercises
    
    print("\t 1) Display the same amount of exercises for each")
    print("\t 2) A particular amount of exercises for each")
    choice = int(input("You choose: "))
    
    if (choice == 1):
        quantity = int(input("How many exercises user needs to practice?"))
        display_addition(quantity)
        display_subtraction(quantity)
        display_multiplication(quantity)
        display_division(quantity)
        
    elif (choice == 2):
        quantity_addition = int(input("Number of exercises for addition: "))
        quantity_subtraction = int(input("Number of exercises for subtraction: "))
        quantity_multiplication = int(input("Number of exercises for multiplication: "))
        quantity_division = int(input("Number of exercises for division: "))

        display_addition(quantity_addition)
        display_subtraction(quantity_subtraction)
        display_multiplication(quantity_multiplication)
        display_division(quantity_division)
        
    else:
        print(" Oops, '{}' isn't defined. Try again!".format(choice))
        request_input_exercices()
