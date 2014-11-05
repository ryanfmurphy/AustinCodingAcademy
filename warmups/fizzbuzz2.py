'''
Tue Nov 4 Warmup: Fizz Buzz Deluxe

Remember the Fizz Buzz problem we worked on in the earlier Homework?

Create a python program that loops through the numbers 1 to 100, prints each number out.

In addition to printing the number, print "fizz" if the number is divisible by 3, and "buzz" if the number is divisible by 5.

If the number is divisible by both 3 and 5, print both "fizz" and "buzz".

We will be recreating the Fizz Buzz program again, but this time making it customizable: What message does the user want to see instead of "fizz" and "buzz"? What numbers should it check divisibility by? Ask the user these questions using raw_input(). If the user doesn't enter anything, use the defaults of "fizz", "buzz", 3 and 5.
'''

fizzword = raw_input('What word shall I show instead of "fizz"? ')
if fizzword == "": fizzword = 'fizz'
buzzword = raw_input('And what word shall I show instead of "buzz"? ')
if buzzword == "": buzzword = 'buzz'
mod1 = raw_input('Print ' + fizzword + ' when divisible by what? ')
if mod1 == "":
    mod1 = 3
else:
    mod1 = int(mod1)
mod2 = raw_input('Print ' + buzzword + ' when divisible by what? ')
if mod2 == "":
    mod2 = 5
else:
    mod2 = int(mod2)

for i in xrange(1,101):
    print i,
    if i % mod1 == 0: print fizzword,
    if i % mod2 == 0: print buzzword,
    print # leave a newline

