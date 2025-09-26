word = input('Enter underscored version: ')

parts = word.split('_')
acc = parts[0]
print(acc)
for each in parts[1:]:
    capitalize = each.capitalize()
    acc += capitalize
    
    
    
