word = input('Enter some words: ')

sepa = word.split()
acc = ' '.join(sepa)
leng = len(sepa)
print(f'"{acc}" has {leng} {"word" if leng==1 else "words"}.')
