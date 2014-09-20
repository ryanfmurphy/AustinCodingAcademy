Python course - Assignment 1 SOLUTIONS
======================================

Conceptual
----------

### Problem 1

1. It's cold but not wet
2. It's not cold but its wet
3. It's neither cold nor wet

### Problem 2

1. `not not True` == `True`
2. `not not False` == `False`

### Problem 3

1. While the password entered is incorrect, continue prompting for the password
2. While the player holds the mouse button, continue charging the laser
3. While the measured temperature is higher than the thermostat temperature,
   continue running the air conditioner.

### Problem 4

10 is an integer, whereas "10" is a string containing the characters '1' and
'0'.

### Problem 5

10 is an integer, whereas 10.0 is a floating point value. Even though their
values are equal, they behave differently in arithmetic operations.

### Problem 6

Some examples of 'numbers' that should not be treated as numeric:

* A phone number
* A social security number
* Insurance policy number

### Problem 7

Returning a value from a function substitutes the returned value in place of the
function call. For example, consider the simple function

    def add(x,y):
        return x+y

Then the expression

    10 + add(2,3)

Can be thought of as

    10 + 5

Since we just think of taking the value returned from calling `add(2,3)`, which
is 5, and substituting it in the place of `add(2,3)`.

A function that simply prints its argument(s) in a special format would not need
a return value.
