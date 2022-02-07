# Lesson_8_task_3_Nazarenko_Dmytro
new_line = input ("Enter new line: ")
new_line = new_line.split()
new_line = "".join(new_line)
dict = {}
for elem in new_line:
    dict[elem] = new_line.count(elem)
print (dict)
sorted_dict = {}
sorted_keys = sorted(dict, key = dict.get)
for elem in sorted_keys:
    sorted_dict[elem] = dict[elem]
for key in sorted_dict:
    print (key, sorted_dict[key], sep = "-")
  