age = 0
dogAge = 0

while(True):
    age = int(input('input age: '))
    if age < 0:
        print('Yout entered a negative number\n')
        continue
    break

if(age < 2): dogAge = age * 10.5
else: dogAge = (2 * 10.5) + ((age - 2) * 4)

print (f'Dog age: {dogAge}')