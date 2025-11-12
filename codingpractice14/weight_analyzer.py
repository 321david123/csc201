def analyzeWeight(weight):
    """
    Analyzes and prints the description of a package weight.
    
    Parameters:
        weight (float): The weight of the package in pounds
    """
    if weight >= 70:
        print("very heavy")
    elif weight >= 10:
        print("heavy")
    elif weight >= 2:
        print("light")
    else:
        print("very light")


def main():
    """
    Main function that allows user to enter package weights
    and analyzes each one until -1 is entered.
    """
    while True:
        weight = float(input("Package weight (-1 to quit): "))
        
        if weight == -1:
            print("Thanks for using weight analyzer")
            break
        
        analyzeWeight(weight)
        print()


if __name__ == "__main__":
    main()

