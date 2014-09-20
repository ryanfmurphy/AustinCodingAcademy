'''
Write a program that prompts the user for a number and determines if that
number was a whole number. You may assume that the number provided
by the user is numeric (you don't need to account for random strings like
'Hello'), but you may only use the functions float() and int() in your logic for
determining if the value is a whole number.
'''

# It's important is to use float() to convert the raw input from the user into
# numeric form. This is because int() can't handle strings with decimal points,
# but float() can handle strings with AND without decimal points.
num_f = float(raw_input("Enter a number: "))

# int() CAN handle floating point values with decimal points, just not strings
# with decimal points. At this point, we're free to get the integer version of
# the user input. Keep in mind that int truncates decimal points. Examples:
# >>> int(10.9)
# 10
# >>> int(10.1)
# 10
# >>> int(10.0)
# 10
num_i = int(num_f)

# If num_f and num_i are the same number, then num_f did not have any values
# truncated in the conversion to int(), meaning it was a whole number.
if (num_f == num_i):
    print("%s is a whole number" % num_f)
else:
    print("%s is a NOT a whole number" % num_f)
