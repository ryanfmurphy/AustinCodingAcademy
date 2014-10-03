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

