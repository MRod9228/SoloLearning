import time

#months_in_year = 12
#weeks_in_year = 52
#days_in_year = 365

current_age = int(input('Enter your current age: '))
end_age = 90
years_left = end_age - current_age
time_left_months = years_left*12
time_left_weeks = years_left*52
time_left_days = years_left*365



print('Let us see how much longer you will be alive!...calculating')

print(f'You have {time_left_days} days, {time_left_weeks} weeks, and {time_left_months} months left...until you are {end_age} years old!')
print('Better start living!', time_left_days, 'days is not long enough')

#To have time to read on cmd
time.sleep(15)