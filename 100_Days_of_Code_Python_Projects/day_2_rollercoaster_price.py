#based on d3l32
from time import sleep
print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input('What is your age? '))
    if age <12:
        print('Child tickets are $5. ')
        bill= 5
    elif age <= 18:
        print('Your ticket will be $7.')
        bill= 7
    elif age >=45 and age <=55:
        print('Everything is going to be ok. Have a free ride on us!')
    else:
        print('Adult tickets are $12.')
        bill = 12
    wants_photo = input('Would you like a photo? Y or N.')
    if wants_photo == 'Y':
        print('There is a fee of $3 ')
        bill += 3
        print('Your total bill is',bill,'dollars!')
    else:
        print(f'Your total is ${bill}.')
else:
    print('Sorry, you cannot ride the rollercoaster')        
sleep(5)
