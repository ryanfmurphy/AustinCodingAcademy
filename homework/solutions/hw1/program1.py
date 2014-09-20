'''
Write a program that prompts the user for their first name, last name, age,
and gender. Print a welcome message which includes their provided information.
Additionally, calculate and print how many years apart you and the user are in
age. You may assume the age provided by the user is a valid integer.
'''

MY_AGE = 23

first = raw_input("What is your first name? ")
last = raw_input("What is your last name? ")
age = int(raw_input("What is your age? "))
gender = raw_input("What is your gender? ")

print("Hey, %s %s!" % (first, last))
print("You're %s years old, and you are %s. Neat!" % (age, gender))

age_diff = MY_AGE - age

# You can use the abs() function to take the absolute value, which simply
# returns the positive version of the value passed in.
# >>> abs(-5)
# 5
# >>> abs(5)
# 5
# This solution assumes you don't know about the abs function.

if age_diff < 0:
    age_diff = age_diff * -1

print("Did you know we are %s years apart?" % age_diff)
