from os import read
import pandas as pd
import string
from string import ascii_uppercase
# Given the file “student_names.txt” do the following:
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
# Read all of the content of the file in one variable.
import os
from itertools import islice
file = open("C:\\Users\\Dell\\Desktop\\education\\CodeLabsAcademy\\names.txt",'r')
students= file.read()
# print(students)
# Write a list of random names to your file.
file1= open("C:\\Users\\Dell\\Desktop\\education\\CodeLabsAcademy\\names.txt",'a+')
file1.write('sofia ouettar\n'+'faten chekman\n'+'lisa tagnit\n')
# display n first lines
n=int(input("how many first lines u wanna display?\n"))
with open("C:\\Users\\Dell\\Desktop\\education\\CodeLabsAcademy\\names.txt",'r') as myfile:
    firstNlines=myfile.readlines()[0:n]
print(firstNlines)
# display n last lines
i=int(input("how many last lines u wanna display?\n"))
with open("C:\\Users\\Dell\\Desktop\\education\\CodeLabsAcademy\\names.txt",'r') as myfile:
    LastNlines=myfile.readlines()[-i:]
print(LastNlines)
 # Search a word in a file
search_word = input("enter a word you want to search in file: ")
if(search_word in students):
  print("word found")
else:
  print("word not found")
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
for i in string.ascii_uppercase :
    with open("C:/Users/Dell/Desktop/education/CodeLabsAcademy/"+i+".txt",'w') as f:
        f.writelines(i)


