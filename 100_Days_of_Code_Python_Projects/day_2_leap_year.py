#based on d3l31
year = int(input('Enter a year: '))
is_leap = int(year%4)
is_not_leap = float
if year % 4 == 0:
    print('leap year')
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else:
            print('not leap year')
    else:
        print('leap year')
else:
    print('not leap year')

