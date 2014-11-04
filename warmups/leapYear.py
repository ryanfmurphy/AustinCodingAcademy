def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return True


def shift_letters(msg, n):
    if len(msg) == 0:
        return "No message to encrypt."
    listOfAscii = [ord(c) + n for c in msg]

    secretCode = "".join([chr(c) for c in listOfAscii])

    return secretCode


'''
for x in range(1000):
    print x, isLeapYear(x)
'''

message = "Znk&rkzzkx&S"
print shift_letters(message, -6)