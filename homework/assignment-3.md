Python course - Assignment 3
============================

Notes
-----

### sets

Sets contain many useful methods for comparing one set to another.

`set1.issubset(set2)` - returns `True` if all the elements of set 1 are
contained in set 2, `False` otherwise.

    >>> first_10 = set([1,2,3,4,5,6,7,8,9,10])
    >>> even_nums = set([2,4,6,8,10])
    >>> even_nums.issubset(first_10)
    True

`set1.intersecton(set2)` - returns a set containing all the elements both in set1
and in set2.

    >>> awesome_animals = set(['lions', 'kittens', 'bears'])
    >>> practical_pets = set(['kittens', 'dogs', 'fish'])
    >>> pets_to_consider = awesome_animals.intersection(practical_pets)
    >>> pets_to_consider
    set(['kittens'])

`set1.difference(set2)` - returns a set containing all the elements in set1
that are not in set2.

    >>> first_10 = set([1,2,3,4,5,6,7,8,9,10])
    >>> even_nums = set([2,4,6,8,10])
    >>> first_10.difference(even_nums)
    set([1, 3, 9, 5, 7])
    >>> even_nums.difference(first_10)
    set([])

`set1.union(set2)` - returns a set containing all the elements either in set1 or
in set2.

    >>> fav_mexican_food = set(['tacos', 'migas', 'enchiladas'])
    >>> fav_japanese_food = set(['sushi', 'ramen'])
    >>> fav_homecooked_food = set(['pork chops', 'chicken and dumplings',
    >>> 'pancakes'])
    >>> fav_food = fav_mexican_food.union(fav_japanese_food).union(fav_homecooked_food)
    >>> fav_food
    set(['migas', 'pancakes', 'enchiladas', 'sushi', 'tacos', 'pork chops', 'chicken
    and dumplings', 'ramen'])

### datetime

To use the datetime module, you must import it.

    >>> import datetime

Getting the current time:

    >>> now = datetime.datetime.now()
    >>> now
    datetime.datetime(2014, 10, 2, 22, 34, 6, 437276)

Printing datetime objects in human readable form: (Use [strftime.net][0] to
create your format specifier)

[0]: http://strftime.net/

    >>> now.strftime("Today is %A %B%e, %Y.")
    'Today is Thursday October 2, 2014.'


To refer to a point in time relative to another point in time ("3 days from
now"), use timedeltas.

    >>> now = datetime.datetime.now()
    >>> tomorrow = now + datetime.timedelta(days=1)
    >>> tomorrow.strftime("Tomorrow is %A %B%e, %Y.")
    'Tomorrow is Friday October 3, 2014.'
    >>> next_week = now + datetime.timedelta(weeks=1)
    >>> next_week.strftime("A week from now will be %A %B%e, %Y.")
    'A week from now will be Thursday October 9, 2014.'

The available arguments to timedelta are:

* seconds
* minutes
* hours
* days
* weeks

Also available if necessary are

* microseconds
* milliseconds



Conceptual problems
-------------------

1) Provide a real world example for each of the following set operations:

* issubset
* intersection
* difference
* union

2) For each statement about time in relation to programming, make a guess as to
whether it's true or false.

* there are always 24 hours in a day
* years have 365 days
* a week always begins and ends in the same month
* the duration of one minute on a computer's clock is the exact same for all
  computers
* a month always begins and ends in the same year
* time has no beginning or end
* The offsets between two timezones remains constant
* Months have either 28, 29, 30, or 31 days
* There is a leap year every year divisible by 4
* The day before Saturday is always Friday
* Time never goes backwards

3) Consider the following dictionary

    data = {
       "results" : [
          {
             "address_components" : [
                {
                   "long_name" : "1600",
                   "short_name" : "1600",
                   "types" : [ "street_number" ]
                },
                {
                   "long_name" : "Amphitheatre Pkwy",
                   "short_name" : "Amphitheatre Pkwy",
                   "types" : [ "route" ]
                },
             ],
             "formatted_address" : "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA",
             "geometry" : {
                "location" : {
                   "lat" : 37.42291810,
                   "lng" : -122.08542120
                },
                "location_type" : "ROOFTOP",
             },
             "types" : [ "street_address" ]
          }
       ],
       "status" : "OK"
    }

describe how you would traverse the dictionary to get the following pieces of
data:

* `"OK"`
* `"Amphitheatre Pkwy"`
* `["route"]`
* `"street_address"`
* `{ "lat" : 37.42291810, "lng" : -122.08542120 }`
* `37.42291810`

Programming
-----------

Before we start on problems, play around with the following function. It allows
you to send a text message to `to_num` with the text `txt_msg`. This function
uses my personal SMS relay which uses the Twilio API. I will only have it open
for use by ACA students for a short period of time!

    import json
    import urllib2

    def send_text_msg(to_num, txt_msg):
        url = 'http://opensms.joequery.me/sms'
        data = json.dumps({'to': to_num, 'body': txt_msg})
        request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
        return urllib2.urlopen(request).read()

We're going to build a sysadmin tool that alerts us when a website we're
managing goes down.

The components to this tool are:

* Determining if a website is responding correctly
* Using time.sleep() to periodically check the web page instead of checking it
  as fast as possible.
* Sending a text message and stopping the program if the website is found to be
  unresponsive.

Each problem should be contained in its own file.

### Problem 1

Create a function that takes a webpage url and a datetime object as an argument,
and returns a string in the form

"Alert! http://joequery.me went down at 10:05AM on 10/2/2014"

In the file, provide some calls to your functions with different datetime
objects and web pages.

For example,

    import datetime

    def get_alert_str(url, dt):
        ### your function code here

    now = datetime.datetime.now()
    print(get_alert_str('www.google.com', now))

    tomorrow = now + datetime.timedelta(days=1)
    print(get_alert_str('www.facebook.com', tomorrow))

### A note on exceptions:

Sometimes situations occur during a program's runtime that the computer cannot
make a decision on what to do next. For example, what if you try to open a file
for reading that does not exist? The computer cannot decide the best course of
action - that's up to you. Do you want to try a different file? Do you want to
stop the program? There are so many options that the computer is forced to
declare it doesn't know how to handle the situation. This "I don't know what to
do!" declaration is called an Exception.

    >>> open('some_file_that_does_not_exist.txt')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IOError: [Errno 2] No such file or directory: 'some_file_that_does_not_exist.txt'

There are many types of exceptions. Exceptions related to input/output fall under
the category of `IOError`. Python determined the file did not exist and threw an
`IOError` with a helpful error message. Unless we "catch" the exception, the
program will abruptly terminate, which is almost never what we want to happen.

The way you account for possible exceptions is through try-except blocks. Try
except blocks have the following structure:

    try:
        Statement that may throw exception
    except TheExceptionThatMightBeThrown:
        What to do if the exception is thrown
     
For example,

    >>> try:
    ...     open('does_not_exist.txt')
    ... except IOError:
    ...     print("Sorry, the file provided does not exist")
    ...
    Sorry, the file provided does not exist

Try to limit the code within the try block to only the relevant lines of code
that may trigger the exception being thrown. Avoid this

    try:
        file_name = raw_input("What file would you like to open: ")
        open(file_name)
    except IOError:
        print("Sorry, the file %s does not exist" % file_name)

Do this instead

    file_name = raw_input("What file would you like to open: ")
    try:
        open(file_name)
    except IOError:
        print("Sorry, the file %s" does not exist" % file_name)

urllib2's urlopen method takes an optional timeout parameter. You can
specify how many seconds you want to wait before an attempted connection is
considered timed out. This is useful because sometimes web applications get stuck
in infinite loops and never return information, which could lock up *your* program
if you're waiting for it to return.

We can test this using a utility called httpbin. If you visit
[http://httpbin.org/delay/2](http://httpbin.org/delay/2) in your browser, it will
delay for 2 seconds and then render information. If you replace 2 with 10, it will
wait 10 seconds. 

Here is an example of urllib2 throwing a timeout exception:

    >>> import urllib2
	>>> urllib2.urlopen("http://httpbin.org/delay/10", timeout=2)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "C:\Python27\lib\urllib2.py", line 127, in urlopen
	    return _opener.open(url, data, timeout)
	  File "C:\Python27\lib\urllib2.py", line 404, in open
	    response = self._open(req, data)
	  File "C:\Python27\lib\urllib2.py", line 422, in _open
	    '_open', req)
	  File "C:\Python27\lib\urllib2.py", line 382, in _call_chain
	    result = func(*args)
	  File "C:\Python27\lib\urllib2.py", line 1214, in http_open
	    return self.do_open(httplib.HTTPConnection, req)
	  File "C:\Python27\lib\urllib2.py", line 1187, in do_open
	    r = h.getresponse(buffering=True)
	  File "C:\Python27\lib\httplib.py", line 1067, in getresponse
	    response.begin()
	  File "C:\Python27\lib\httplib.py", line 409, in begin
	    version, status, reason = self._read_status()
	  File "C:\Python27\lib\httplib.py", line 365, in _read_status
	    line = self.fp.readline(_MAXLINE + 1)
	  File "C:\Python27\lib\socket.py", line 476, in readline
	    data = self._sock.recv(self._rbufsize)
	socket.timeout: timed out

To catch the exception, we need to import the socket library

    >>> import socket
	>>> try:
	...     urllib2.urlopen("http://httpbin.org/delay/10", timeout=2)
	... except socket.timeout:
	...     print("Operation timed out!")
	...
	Operation timed out!

Whenever you request a website from a server, it will send back a response code
informing you about the nature of the response. These response codes can let us
know if the server had a problem fulfilling our request. If a response code
indicating failure is sent back, urllib2 throws an HTTPError

	>>> urllib2.urlopen("http://google.com/some-page-that-does-not-exist")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "C:\Python27\lib\urllib2.py", line 127, in urlopen
	    return _opener.open(url, data, timeout)
	  File "C:\Python27\lib\urllib2.py", line 410, in open
	    response = meth(req, response)
	  File "C:\Python27\lib\urllib2.py", line 523, in http_response
	    'http', request, response, code, msg, hdrs)
	  File "C:\Python27\lib\urllib2.py", line 442, in error
	    result = self._call_chain(*args)
	  File "C:\Python27\lib\urllib2.py", line 382, in _call_chain
	    result = func(*args)
	  File "C:\Python27\lib\urllib2.py", line 629, in http_error_302
	    return self.parent.open(new, timeout=req.timeout)
	  File "C:\Python27\lib\urllib2.py", line 410, in open
	    response = meth(req, response)
	  File "C:\Python27\lib\urllib2.py", line 523, in http_response
	    'http', request, response, code, msg, hdrs)
	  File "C:\Python27\lib\urllib2.py", line 448, in error
	    return self._call_chain(*args)
	  File "C:\Python27\lib\urllib2.py", line 382, in _call_chain
	    result = func(*args)
	  File "C:\Python27\lib\urllib2.py", line 531, in http_error_default
	    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
	urllib2.HTTPError: HTTP Error 404: Not Found

You can use httpbin to emulate error codes. 200 is the code for 'OK', or no error.
404 means the resource was not found. 500 means there was an application error.

	>>> urllib2.urlopen("http://httpbin.org/status/200")
	<addinfourl at 39465992L whose fp = <socket._fileobject object at 0x0000000002526E58>>
	>>> urllib2.urlopen("http://httpbin.org/status/500")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "C:\Python27\lib\urllib2.py", line 127, in urlopen
	    return _opener.open(url, data, timeout)
	  File "C:\Python27\lib\urllib2.py", line 410, in open
	    response = meth(req, response)
	  File "C:\Python27\lib\urllib2.py", line 523, in http_response
	    'http', request, response, code, msg, hdrs)
	  File "C:\Python27\lib\urllib2.py", line 448, in error
	    return self._call_chain(*args)
	  File "C:\Python27\lib\urllib2.py", line 382, in _call_chain
	    result = func(*args)
	  File "C:\Python27\lib\urllib2.py", line 531, in http_error_default
	    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
	urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR

You can catch multiple exceptions at one time:

    except (Exception1, Exception2):

### Problem 2

Create a function called `is_website_status_ok` that takes a url and a timeout
value as an argument. The function should return `True` if the website appears
ok, and `False` if the page times out or if there is an error retrieving the page.

### Problem 3

Create a program which allows the user the enter a website url they want to monitor,
and a 10 digit US phone number to text if the website seems to not respond correctly.
Ask the user how often in seconds they want the script to check the website status.
Do not let this number be smaller than 30 seconds.

The program should be able to run forever assuming there is no errors reported. If the
website does appear to go down, the program should send a text alert to the number
provided by the user, and then the program should stop running.

Here are some helper functions you should use in the assignment:

	>>> def is_valid_us_phone(phone):
	...     nums_only = "".join(c for c in phone if c.isdigit())
	...     return len(nums_only) == 10
	...
	>>> is_valid_us_phone('9021317761')
	True
	>>> is_valid_us_phone('90313071')
	False

The following function will help emulate a website randomly going down. Pass in the
normal url you want to check as an argument. 70% of the time the function will return
the provided url. The other 30% it will return an httpbin url that results in a 500
error code. While this function should not be in the final product, you should use it
to test your program's correctness.

	>>> def emulate_random_meltdown(url):
	...     error_url = "http://httpbin.org/status/500"
	...     from random import randint
	...     i = randint(1,10)
	...     if i <= 3:
	...         return error_url
	...     else:
	...         return url
	...
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://www.google.com/'
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://httpbin.org/status/500'
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://httpbin.org/status/500'
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://www.google.com/'
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://www.google.com/'
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://www.google.com/'
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://www.google.com/'
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://www.google.com/'
	>>> emulate_random_meltdown("http://www.google.com/")
	'http://httpbin.org/status/500'
