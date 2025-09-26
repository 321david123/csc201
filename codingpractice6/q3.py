sentence = input('Enter a sentence: ')

words = sentence.split()
acc = 0 
for word in words: 
    acc+= len(word)
    
average = acc/len(words)

print(f'The average word length is {average:.3f}')


#This code basically takes a sentence and then splits it into words and then calculates the average word length, finally prints the
#average word length with 3 decimals