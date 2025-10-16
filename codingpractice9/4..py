def dotDash(string):
    if len(string) % 2 == 0:
        for i in range(len(string)):
            return '-' + '-'.join(string) + '-'
    else:
        for i in range(len(string)):
            return '.' + '.'.join(string) + '.'

def main():
    string = input('Enter a string: ')
    print(dotDash(string))

main()