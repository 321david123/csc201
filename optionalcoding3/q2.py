goals=int(input('How many fields goals were made this week? '))
acc=0
for i in range(goals):
    point = int(input(f'How many yards was field goal number {i+1}? '))
    if point >= 50:
        acc+=5
    elif point >= 40:
        acc+=4
    else:
        acc+=3
extra=int(input('How many extra points were made this week? '))
missed=int(input('How many field goals were missed this week? '))

total = acc + extra - missed
poin,week = '',''
if total == 1:
    poin = 'point'
else:
    poin = 'points'
if total > 10:
    week = 'great'
elif total >= 7:
    week = 'good'
elif total >= 3:
    week = 'typical'
else:
    week = 'mediocre'
    
    
print(f'\nYour kicker earned {total} {poin} and had a {week} week.')