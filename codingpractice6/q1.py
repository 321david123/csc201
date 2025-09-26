phone = input('Enter a 10 digit phone number: ')

part1 = phone[:3]
part2 = phone[3:6]
part3 = phone[6:]

print(f'({part1}) {part2}-{part3}')