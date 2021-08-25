#1. Create a greeting for your program.
#--Done
#2. Ask the user for the city that they grew up in.
#--Done
#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

import time
print("""               Band Name Generator 
    Enter city name and pet name for a custom band name!
            Letter or Numbers -allowed""" )
city_name = str(input('Enter what city you were born in: '))
pet_name = str(input('Enter the name of your pet: '))
band_name = print('Your band name is:--'+city_name+pet_name + '--')

print(band_name)
print('     ')
print('Closing in 5 seconds!')
secs = 5
while secs != 0:
    print(secs)
    time.sleep(1)
    secs-=1
    if secs ==0:
        print('Bye!')


