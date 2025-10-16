def convertDateFormat(date):
    day = date[:2]
    month = date[2:4]
    year = date[4:]
    return month+'/'+day+'/'+year
def main():
    date = input('Enter a date in the format DDMMYYYY: ')
    print(f'The date is {convertDateFormat(date)}')
main()