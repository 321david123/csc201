scores = int(input('Enter number of scores: '))
if scores == 0:
    print('\nNo scores were entered!')
else:
    acc=0
    maxS=0
    for i in range(scores):
       score = int(input('Enter quiz score: '))
       acc+=score
       if score > maxS:
           maxS=score
    avg = acc / scores
    print(f'\nquiz average: {avg:.1f}\nmax quiz score: {maxS}')


#This code basically takes a number of scores and then takes the scores and calculates the average and the max score, finally prints the
#average and max score with 1 decimal place