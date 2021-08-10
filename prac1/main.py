# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# ex1
student_grades = {'Adam':'CR', 'Leo':'HD', 'Max':'D', 'Nicole':'CR', 'Oscar':'P'}

for k, v in student_grades.items():
    print(k, v)
    print('(\'%s\',\'%s\')' % (k, v))


# ex4
import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


# ex5
list = ['Apple', 'Banana', 'Fig', 'Pear', 'Plum', 'Peach', 'Raspberry']
print('Before:', list)
list.pop(-1)
print('After', list)
list.pop(0)
print('After', list)


# ex6
with open('input.txt') as f:
   file = open('output.txt', 'w')
   for line in f:
       print(line)
       file.write(line)

