number = input('Enter a two digit number to sum: ')

if len(number) != 2:
    print('Your number must be two digits long!')
    exit()
   
print('You choose number: ' + str(number))
num1 = int(number[0])
num2 = int(number[1])
the_sum = num1 + num2
print(the_sum)
