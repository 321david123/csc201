import math
rad = int(input("Enter largest radius: "))
for i in range(1,rad + 1):
    print(f'{i} v: {round(4/3 * (math.pi * i**3), 2)}')
    