#Faça um algoritmo que receba 3 (três) notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas.

print("-----------------------------------")
print("Weighted average mean of grades")
print("-----------------------------------")

first_grade = float(input("\nInsert the first grade: "))
weight_one = int(input("Which weight has this grade? "))

second_grade = float(input("\nInsert the second grade: "))
weight_two = int(input("Which weight has this grade? "))

third_grade = float(input("\nInsert the third grade: "))
weight_three = int(input("Which weight has this grade? "))

first_grade_weight = first_grade * weight_one
second_grade_weight = second_grade * weight_two
third_grade_weight = third_grade * weight_three

sum_of_products = first_grade_weight + second_grade_weight + third_grade_weight
sum_of_weights = weight_one + weight_two + weight_three

weighted_average_mean = sum_of_products / sum_of_weights

print("\nThe average is {:.2f}".format(weighted_average_mean))
