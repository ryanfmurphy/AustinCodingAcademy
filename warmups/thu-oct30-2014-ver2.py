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

# this is version 2
# it has differences

