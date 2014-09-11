Python course - Assignment 1
============================

Conceptual
----------

1) List all three possible scenarios in which the following statement is false:

    "It's cold and wet outside"

2) If the expression `not True` evaluates to False, and the expression `not
False` evaluates to True, what is the value of `not not True`? What is the value
of `not not False`?

3) Provide three real world scenarios where a while loop would be appropriate

4) Explain the difference between the following values:

    10
    "10"

5) Explain the difference between the following values:

    10
    10.0

6) When you assign an integer to a variable in Python, the computer internally
stores the integer value in a specific format that allows us to perform math
operations between the value and other integers. However, the computer has a
limit to what size integer it can store. For example, A 32bit operating system
that wishes to allow for negative integers can only store up to the value
2147483648. Attempting to store the value 2147483649 can lead to unpredictable
and potentially devastating consequences! With this knowledge, can you think of
a type of number you encounter in everyday life that would best be represented
by a string instead of an integer? Would you ever perform arithmetic with this
type of number?

Hint: Count the number of digits in the numbers provided. What other numbers do
you commonly see with this exact number of digits?

7) Explain in your own words what returning a value from a function does.
Provide an example of when you would want a function to return a value, and
provide an example of when a return value is not necessary.


Programs
--------

1) Write a program that prompts the user for their first name, last name, age,
and gender. Print a welcome message which includes their provided information.
Additionally, calculate and print how many years apart you and the user are in
age. You may assume the age provided by the user is a valid integer.

2) Write a program that prompts the user for a number and determines if that
number was an integer or floating point. You may assume that the number provided
by the user is numeric (you don't need to account for random strings like
'Hello'), but you may only use the functions float() and int() in your logic for
determining if the value is an integer or floating point.

Hint: Observe the following shell session

    >>> float(2.5)
    2.5
    >>> int(2.5)
    2
    >>> 2.0 == 2
    True

3) Your manager orders Austin's Pizza every Friday for you and your fellow
coworkers. You're getting tired of figuring out how many pizzas you need to buy,
so you decide to automate the process. You're also getting tired of Austin's
Pizza and would prefer East Side Pies, but complaining about free food doesn't
set you up well for a promotion. Create a program which lets the user input the
number of people eating, the number of slices each will eat, and the number of
slices per box of pizza. The program should print out the minimum number of
pizza boxes necessary to feed the office based on the values provided.

4) FizzBuzz is a classic technical interview problem. Complete the exercise as
stated below:

    Write a program that prints the numbers from 1 to 100. But for multiples of
    three print 'Fizz' instead of the number and for the multiples of five print
    'Buzz' For numbers which are multiples of both three and five print
    'FizzBuzz'

5) Fortune cookie ASCII frame

### PART 1

Create a program containing a function called print_ascii_frame that has an
argument named `message`.

    def print_ascii_frame(message):
        # ...
        # ...

This function should create and print an ASCII art border around the message
passed in. For example, the following function call

    print_ascii_frame('My name is Joe!')

Would result in something resembling

    |=====================|
    |                     |
    | ~ My name is Joe! ~ |
    |                     |
    |=====================|

The function should be able to handle strings of arbitrary length.

Hints:

You can use len() to get the number of characters in a string...

    >>> len('hello')
    5

Observing that multiplying a string returns the string repeated that many times...

    >>> "=" * 30
    '=============================='

### PART 2

Now that you have your ascii frame function finished, it's time to frame a
noteworthy phrase. We're going to grab some fortune cookies phrases from the
internet.

The following function scrapes the website www.fortunecookiemessage.com to
get a random fortune (you do not have to understand how the function works yet):

    def get_random_fortune():
        import urllib2
        fortune_url = 'http://www.fortunecookiemessage.com'
        resp = urllib2.urlopen(fortune_url)
        html = resp.read()

        start_flag = 'cookie-link">'
        fortune_start =  html.index(start_flag) + len(start_flag)
        fortune_end = html.index('<', fortune_start)
        fortune =  html[fortune_start:fortune_end]
        if not fortune or len(fortune) > 70:
            return get_random_fortune()
        else:
            return fortune

The function returns a string representing the retrieved fortune

    >>> my_fortune = get_random_fortune()
    >>> my_fortune
    'In human endeavor, chance favors the prepared mind.'

Copy and paste the function to the top of your the file where your
print_ascii_frame function is defined.

Combine your print_ascii_frame function and the get_random_fortune function to
create a program that downloads a fortune from the internet and frames it with
your fancy ASCII art border.

Below are a few sample runs of my version of the program, which I have saved in
a file called fortune.py:

    ~$ python fortune.py
    |============================|
    |                            |
    | ~ You love Chinese food. ~ |
    |                            |
    |============================|

    ~$ python fortune.py

    |=========================================================================|
    |                                                                         |
    | ~ A short stranger will soon enter your life with blessings to share. ~ |
    |                                                                         |
    |=========================================================================|

    ~$ python fortune.py
    |=========================================|
    |                                         |
    | ~ Great thoughts come from the heart. ~ |
    |                                         |
    |=========================================|
