def reverseOrder(name):
    completeName = name.split()
    name = completeName[0]
    lastN = completeName[1]
    return lastN + ', ' + name
    
def main():
    names = int(input('How many names? '))
    for i in range(names):
        name = input('Enter full name beginning with first name: ')
        print(f'Reversed it is {reverseOrder(name)}')
main()