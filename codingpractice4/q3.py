num = int(input("Enter number of numbers to process: "))
positiveacc, negativeacc, count1,count2 = 0,0,0,0
for i in range(num):
    num = float(input("Enter number: "))
    if num < 0:
        negativeacc += num
        count1+=1
    elif num > 0:
        positiveacc +=num
        count2+=1
print(f'\nThere were {count2} positive numbers summing to {positiveacc}\nThere were {count1} negative numbers summing to {negativeacc}')
        