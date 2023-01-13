import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

import math

name = input("\nEnter your Name: ")
age = input("\nHow old are you: ")
cgpa = input("\nGive your CGPA: ")

print ("\nYour name is: ",name)
print("Your age: ", age)
print("CGPA is: ", cgpa) #this is comment