sect = int(input("How many sections of this course? "))
sum = 0
for i in range(sect):
    stud = int(input(f'Number of students in section {i+1}: '))
    sum+=stud
print(f'\nTotal number of students: {sum}')