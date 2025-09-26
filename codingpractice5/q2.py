word = input('Enter a word: ')
print(f'{str.capitalize(word)} has {len(word)} characters.')
for i in range(len(word)):
    print(f'{str.capitalize(word[i])}')