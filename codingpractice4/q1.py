import math

def main():
    leg1 = float(input("Enter leg 1: "))
    leg2 = float(input("Enter the leg 2: "))
    hypo = math.sqrt((leg1**2) + (leg2**2))
    
    print(f'\nA right triangle with legs {leg1} and\n{leg2} has hypotenuse {round(hypo, 2)}')
    
main()