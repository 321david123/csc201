def main():
    x = 5
    y = 50
    a = 1
    for z in range(1, 6, 2):
        x = x + z
        print('x =', x)
        y = y - x
        print('y =', y)
        a = a * z
    print('a =', a)

main()