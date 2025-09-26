nums = int(input("How many numbers are we looking at? "))

for i in range(nums):
    nums = int(input("\nEnter a number: "))
    if nums % 2 == 0:
        print("It's even!")
    else:
        print("It's odd!")
    if nums % 3 == 0: 
        print("It's divisible by 3!")