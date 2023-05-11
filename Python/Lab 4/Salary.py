import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

print("Enter employe name: ")
name = input()

print("Enter employe salary: ")
salary = input()

print("Enter employe Service in year")
year = input()

if(int(year) > 10):
    total = int(salary) + (int(salary)*15)/100
    print(total)
else:
    print (salary)