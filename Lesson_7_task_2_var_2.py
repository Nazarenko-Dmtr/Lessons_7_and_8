# Lesson_7_task_2_Nazarenko_Dmytro_var_2_full_name

name = input("Enter your name:  ")
name = name.lower()
for _ in name:
    name = name.replace(" ", "A")
while not name.isalpha():
    name = input("Only literals are acceptable. Try again:  ")
name = name.split("A")
name = " ".join(name)
print(name.title())
