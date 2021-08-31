import random
import time
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(names)
nums = len(names)


rand_num = random.randint(0, nums-1)
lucky_one = names[rand_num]
print(lucky_one + " is going to be buying the meal today.")
time.sleep(5)