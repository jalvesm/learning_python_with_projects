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
    

print("----------------------------------")
print("MATHEMATICS EXERCISES GENERATOR")
print("----------------------------------")

print("A)ADDITION:")
print("1. Solve the addition exercises bellow:\n")
for addition_exercises in range(1, 10):
    generates_addition_exercise()
    
print("B). SUBTRACTION:")
print("1. Solve the subtraction exercises bellow:\n")
for subtraction_exercises in range(1, 10):
    generates_subtraction_exercise()
    
print("C) MULTIPLICATION:")
print("1. Solve the multiplication exercises bellow:\n")
for addition_exercises in range(1, 10):
    generates_multiplication_exercise()
    
print("C) DIVISION:")
print("1. Solve the division exercises bellow:\n")
for subtraction_exercises in range(1, 10):
    generates_division_exercise()
