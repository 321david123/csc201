def areBothEven(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return True
    else:
        return False

def main():
    times = int(input('How many pairs? '))
    
    for i in range(times):
        n1 = int(input('\nEnter first number: '))
        n2 = int(input('Enter second number: '))
        
        if areBothEven(n1,n2) == True:
            print(f'Sum is {n1+n2}')
        else:
            print(f'Product is {n1*n2}')
            
    
main()