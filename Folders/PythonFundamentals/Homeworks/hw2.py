from os import read
import pandas as pd
# Given the file “student_names.txt” do the following:
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
# Read all of the content of the file in one variable.
import os
from itertools import islice
file = open("C:/Users/Dell/Desktop/education/CodeColab/student_names.txt",'r')
students= file.read()
# print(students)
# Write a list of random names to your file.
students= students + "\nsofia ouettar"+"\nbakhouche amel"+"\nchekman faten"
file1= open('C:/Users/Dell/Desktop/education/CodeColab/student_names.txt','a')
file1.write(students)
# display n lines
n=int(input("how many lines u wanna display?\n"))
for i  in range(n):
  line=file.readline(i)
  print(line)
  # Search a word in a file
search_word = input("enter a word you want to search in file: ")
if(search_word in students):
  print("word found")
else:
  print("word not found")
  # didnt really know how to iterate over alphabet
file = open("C:/Users/Dell/Desktop/education/CodeColab/A.txt",'x')