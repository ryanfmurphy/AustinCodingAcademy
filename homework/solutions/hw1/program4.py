# FizzBuzz is a classic technical interview problem. Complete the exercise as
# stated below:
#
#     Write a program that prints the numbers from 1 to 100. But for multiples of
#     three print 'Fizz' instead of the number and for the multiples of five print
#     'Buzz' For numbers which are multiples of both three and five print
#     'FizzBuzz'
#

# Using a while loop
i = 1
while i <= 100:
    # It's important to have this compound condition first. If you have it on
    # the bottom, it will never be reached!
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

    i += 1

# Using a for loop
for i in xrange(1, 100+1): # 101 exclusive == 100 inclusive
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
