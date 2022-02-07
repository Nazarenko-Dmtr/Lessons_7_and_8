# Lesson_8_task_2_add_Nazarenko_Dmytro
roman_arabic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100}
roman_number = input ("Enter roman number: ")
roman_number = roman_number.upper()
print (roman_number)
new_list = []
for i in roman_number:
    if i in roman_arabic:
        new_list.append(roman_arabic[i])
    else:
        print ("Enter correct literals: ")
        roman_number = input ("Enter roman number: ")
print (new_list)
final_list = []
shouldSkip = False
for i in range (len(new_list)):
    if shouldSkip:
        shouldSkip = False
        continue
    if i < len (new_list) - 1 and new_list [i] < new_list [i + 1]:
        final_list.append(new_list [i + 1] - new_list [i])
        print (new_list [i + 1] - new_list [i])
        shouldSkip = True
    else: 
        final_list.append(new_list [i])
        print(new_list [i])
print (final_list)
print(sum(final_list))
