name = input('Enter your full name: ')

parts = name.split()
part3 = parts[2]

username = parts[0][0] +'.'+ parts[1][0] +'.'+ part3
if len(username) > 15:
    username = username[:15]

print(f'Username is {username.lower()}')



#This code basically takes a name and then creates a username by lowering everything, taking the first letter
#of the first name and last name and then the third last name is added to the username everything separated by a period.