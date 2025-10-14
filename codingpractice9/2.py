import math
def computeVolume(radius):
    return (4/3)*math.pi * (radius**3)

def main():
    radius = float(input('Enter the radius of a sphere: '))
    print(f'The volume is {computeVolume(radius):.3f}')
main()