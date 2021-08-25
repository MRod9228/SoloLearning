import time#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

bill = float(input('Please enter the bill ammount: '))
people = int(input('Please enter the number of people: '))
#says to use 12%
bill_after_tip = 12 / 100 * bill + bill
per_person = bill_after_tip/people
#tip_percentage = before_tip*(*100)
#pay_per_person = before_tip*tip_percentage
print('{:.2f}'.format(per_person))
#had an issue trying to figure our the format there...had to google it
time.sleep(10)
