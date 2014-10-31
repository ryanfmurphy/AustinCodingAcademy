Warmup Tue Oct 30 2014
======================

1. Leap Years
-------------

Write a function that determines whether a year is a Leap Year.

### Which Years are Leap Years? ###
In the Gregorian calendar 3 criteria must be taken into account to identify leap years:

* The year is evenly divisible by 4;
* If the year can be evenly divided by 100, it is NOT a leap year, unless;
* The year is also evenly divisible by 400. Then it is a leap year.


2. Secret Codes
---------------

Create a function `shift_letters(msg, n)` that takes a string msg and "shifts" each character by n by: (1) converting it to a number, (2) adding n to the number and (3) converting it back to a letter.  Return the resulting string.

### Example ###
```python
shift_letters("hello world",1) # => 'ifmmp!xpsme'

# you can go backwards, too!
shift_letters("ifmmp!xpsme",1) # => 'hello, world'
```

Hint: You can use `ord()` to convert a character into it's corresponding ASCII number code, and then `chr()` will convert the number back to a character.

### Example ###
```python
ord('a') # => 97
chr(97) # => 'a'

ord('b') # => 98
chr(98) # => 'b'

ord('c') # => 99
chr(99) # => 'c'
```

Now use your `shift_letters()` function to figure out the answer to this riddle:

    Q: What occurs once in a minute, twice in a moment and never in one thousand years?

    A: Znk&rkzzkx&S


Solution
--------

```python
def leap_year(year):
    # if it is div by 4, then is a leap_year
    #   EXCEPT if div by 100, then not a leap_year
    #     EXCEPT if div by 400, then is actually a leap_year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                x = True
            else:
                x = False
        else:
            x = True
    else:
        x = False
    return x

def shift_letters(msg, n):
    # convert all the characters in the msg into numbers using ord()
    # add n to each of the numbers
    numbers = [ord(c) + n for c in msg]
    # convert those numbers back into characters with chr()
    chars = [chr(n) for n in numbers]
    # put that back into a string a return it
    return ''.join(chars)
```




