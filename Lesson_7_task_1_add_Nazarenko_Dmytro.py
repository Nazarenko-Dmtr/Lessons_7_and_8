# Lesson 7, task 1 add 
# WORKS FOR ALL WORDS, EXCEPT WORDS WITH EQUAL NUMBER > 1 OF EACH ELEMENTS IN WORD (FOR EXAMPLE - ABBA)
word = input("enter any word: ") 
from random import randint
text = word * randint (1, 20) # Line written by Vovochka
print (text)
frequence_of_elements_in_text = [] # How many times each unique element repeats in text
for elem in set(text):
    frequence_of_elements_in_text.append(text.count(elem))
print (frequence_of_elements_in_text)
from math import gcd
from functools import reduce
max_common_divider = reduce(gcd,frequence_of_elements_in_text) 
print(max_common_divider)
word_length = len(text) // max_common_divider
least_word = text [: word_length]
print (least_word)
