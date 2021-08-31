#from 100 days of code with angela #Day 4
import time

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) #the first number in the two digit input
vertical = int(position[1])   #the second number in the two digit input

map[vertical - 1] [horizontal - 1]= "X"

print(f"{row1}\n{row2}\n{row3}")
time.sleep(5)