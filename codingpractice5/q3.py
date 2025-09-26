print("Enter the daily low temperatures for a week.\n")
max=100
min=-100
for i in range(7):
    temp = int(input(f'Low temp day {i+1}: '))
    if temp < max:
        max=temp
    if temp > min:
        min=temp
print(f'\nThe greatest low temp: {min}\nThe lowest low temp: {max}')