#input
magnitude = 0
descriptor = ""
while(True):
    magnitude = float(input('Input magnitude: '))
    if magnitude < 0:
        print('Magnetude can\'t be less than 0\n')
        continue
    break
    
#output
print()
if magnitude < 2:
    descriptor = 'Micro'
elif magnitude > 2 and magnitude < 3:
    descriptor = 'Very minor'
elif magnitude > 3 and magnitude < 4:
    descriptor = 'Minor'
elif magnitude > 4 and magnitude < 5:
    descriptor = 'Light'
elif magnitude > 5 and magnitude < 6:
    descriptor = 'Moderate'
elif magnitude > 6 and magnitude < 7:
    descriptor = 'Strong'
elif magnitude > 7 and magnitude < 8:
    descriptor = 'Major'
elif magnitude > 8 and magnitude < 10:
    descriptor = 'Great'
elif magnitude > 10:
    descriptor = 'Meteoric'

print(f'An earthquake of this magnitude is {descriptor}')