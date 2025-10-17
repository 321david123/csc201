def greatSeven(number1, number2):
    if number1 == 7:
        return True
    if number2 == 7:
        return True
    if number1 + number2 == 7:
        return True
    if number1 - number2 == 7:
        return True
    if number2 - number1 == 7:
        return True
    else:
        return False

print(greatSeven(3,3))