#                   based on d3l35
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
from time import sleep
name1 = input('Please enter person 1 first and last name: ')
name2 = input('Please enter person 2 first and last name: ')

t = int(name1.count('t') + int(name2.count('t')))
r = int(name1.count('r') + int(name2.count('r')))
u = int(name1.count('u') + int(name2.count('u')))
e = int(name1.count('e') + int(name2.count('e')))

total_true = str(t+r+u+e)
print('Total true = ',total_true)

l = int(name1.count('l') + int(name2.count('l')))
o = int(name1.count('o') + int(name2.count('o')))
v = int(name1.count('v') + int(name2.count('v')))
e = int(name1.count('e') + int(name2.count('e')))

total_love = str(l+o+v+e)
print('Total love = ',total_love)

love_score = int(total_true+total_love)
#print(f'Your love score is: {love_score}')
if love_score <10 or love_score >90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score >=40 and love_score <=50:
    print(f'"Your score is {love_score}, you are alright together."')
else:
    print(f"Your score is {love_score}.")

sleep(5)
