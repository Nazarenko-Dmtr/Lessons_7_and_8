# Lesson_7_task_2_Nazarenko_Dmytro_var_1_name_only

name = input("Enter your name:  ")
while not name.isalpha():
    name = input("Only literals are acceptable. Try again:  ")
print(name.capitalize())
