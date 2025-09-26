integer = int(input("Enter an integer: "))
sum = 0
for i in range(1,integer,2):
    sum+=i
print(f'Sum of the odds is {sum}')