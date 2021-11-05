#based on d3l33
#------Instructions------
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1
from time import sleep

print('Welcome to python pizza deliveries!')
size = input('What size pizza do you want? S, M or L ')
add_pepperoni = input('Do you want pepperoni? Y or N')
extra_cheese = input('Do you want extra cheese? Y or N')
total = 0

bill = 0

if size == 'S':
  bill += 15
elif size == 'M':
  bill += 20
elif size == 'L':
    bill+= 25
elif bill != 'S' or 'M' or 'L':
  print('HMMM, Looks like you didn\'t select a size!')

if add_pepperoni == 'Y':
  if size == 'S':
    bill += 2
  else:
    bill += 3
    
if extra_cheese == 'Y':
  bill += 1
  
print(f'Your final bill is: ${bill}.')
sleep(5)
