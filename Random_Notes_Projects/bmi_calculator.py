# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

# Warning you should convert the result to a whole number.

#variables

weight = float(input('Enter your weight in (kg): '))
height = float(input('Enter your height in (m): '))
formula = weight/(height*2)

print(weight)
print(height)
print(formula)