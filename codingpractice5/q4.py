act = int(input('Enter the actual time: '))
alarm = int(input('Enter the alarm time: '))

time1=(act//100 * 60) + act%100
time2=(alarm//100 * 60) + alarm%100
remainder=time2-time1
if remainder>0:
    print(f'{remainder} minutes still to sleep!')
else:
    print(f'Turn off the alarm!')