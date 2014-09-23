Python course - Assignment 2
============================

Conceptual
----------

1) Provide 3 real-world examples of programs that need to read in
the contents of a file as opposed to asking the user directly for input.

2) You are designing the next greatest PC game, HarmVille. HarmVille
is like FarmVille, but with a Grand Theft Auto twist. When a user installs
the game, they are given a choice of what directory they would like to
install the game. On Windows operating systems, this defaults to
C:\Program Files, but the user is free to choose any directory. The directory
structure of the game is as follows:

    HarmVille
	| HarmVille.exe
	| README
	| uninstall.exe
	| assets
	  | images
	  | models
	  | terrain
	  
When writing the game source, should developers use absolute or relative
file paths to refer to files in the assets directory? Explain your reasoning.

3) Suppose append mode did not exist in regards to writing to a file. How 
would you emulate appending to a file using only read and write modes? (No 
code required, just describe your strategy). What is a potential issue with 
this strategy?

4) Describe the impact of having to use the strategy described in problem 3
if multiple programs wanted to append to the same file at the same time.

5) CSV, which stands for comma-separated values, is a simple file format for 
storing tabular data in plaintext form. It's extremely useful since many 
spreadsheet applications understand the CSV format, and it's very simple
for even beginner programmers to create CSV files. Below is an example CSV
file

    Year,Make,Model,Description,Price
    1997,Ford,E350,Good condition,3000.00
    1999,Chevy,Venture,Runs great,4900.00
    1996,Jeep,Grand Cherokee,Seen better days...,4799.00
	
Can you think of a value for the Description column that could introduce 
problems for programs attempting to interpret the CSV data? How would you 
remedy this problem?

6) Explain the following terms in relation to lists:

    1) element
	2) index
	3) iterate
	4) append

7) A set is a data structure similar to a list, but the elements of a set
have no concept of order. However, evaluating if a set contains a specific
value is much faster than evaluating if a list contains a specific value.
Describe a scenario that would be a good use case for a set, and explain
why you would choose using a set over using a list. Similarly, describe a
scenario that would be a good use case for a list, and explain why you would
choose to use a list over using a set.

8) What are three characteristics of well designed functions?

9) Self-documenting code is code that uses *meaningful* naming to document
the intention of the code as much as possible. Rewrite the following code
to be self documenting. The code should contain no comments.


    import urllib2

    def foo(x,y):
	    '''
		This function attempts to download the web page at the url specified
		in the `x` argument. The function saves the web page to the file path
		specified by the `y` argument.
		'''
		baz = urllib2.urlopen(x).read()
		with open(y, 'w') as f:
		    f.write(baz)
		
	h = raw_input("Enter the web page you would like to download: ")
	z = raw_input("Enter the file path where the web page should be saved: ")
	foo(h,z)
	
Here is an example run of this program

    Enter the web page you would like to download: http://joequery.me
    Enter the file path where the web page should be saved: page.html
	
10) Provide dictionaries representing the following objects:

    1) An air conditioner
	2) An Amazon shopping cart
	3) A computer
	
Each dictionary should contain at least 4 keys, but more are encouraged!

11) Without providing specific examples, explain in general terms when you would
use a list over a dictionary, and when you would use a dictionary over a list.

Helpful built-in methods
-----------------------

Here are some helpful built-in methods that you may use in your
programming solutions!

### String methods

.strip(): Returns the string without trailing newline characters.

    >>> "hello\n".strip()
    'hello'
	
NOTE: This does not modify the string, but merely returns a new string.
You will need to assign this return value to a variable if you wish to use
the value later. Example:

	>>> name = "Joseph\n"
	>>> name.strip()
	'Joseph'
	>>> name
	'Joseph\n'
	>>> name = name.strip()
	>>> name
	'Joseph'
	
.split(delimeter): Returns a list representing the string separated by
every occurrence of the delimeter within the string. 

    >>> "1:2:3".split(":")
    ['1', '2', '3']
    >>> "heyhatherehaperson".split("ha")
    ['hey', 'there', 'person']
	
.startswith(s): Returns True if the string starts with the string `s`. Returns
False otherwise

    >>> "hello".startswith("hell")
    True
    >>> "hello".startswith("x")
    False
	
.isspace(): Returns True if the string is a whitespace string. Returns False
otherwase.

    >>> "\n".isspace()
	True
	>>> "w".isspace():
	False
	
### List methods

.count(value): Returns the number of times value is contained in the list.

    >>> [0,1,1,2,3].count(1)
    2
	
### File methods

.read(n): Read and return n bytes from a file. 1 byte == 1 character for files
with no special accented characters. If the end of the file is found, the empty
string is returned.

    >>> with open('stuff.txt') as f:
            print(f.read(1))
			
	i

	
Programs
--------

1) Create a program which continuously prompts the user to enter numbers until
they type in a phrase of your choice. Calculate and print the mean, median, and
mode of the numbers provided.
	
2) Create a program which prints each non-whitespace character of a file in a
zig-zag pattern. For example, for a file that begins like

    import inspect
    class DynamicRouter(routers.DefaultRouter):
	    def get_routes(self, viewset):
		...
		...
		
The output should resemble

	i
	 m
	  p
	   o
		r
		 t
		  i
		   n
			s
			 p
			  e
			 c
			t
		   c
		  l
		 a
		s
	   s
	  D
	 y
	n
	 a
	  m
	   i
		c
		 R
		  o
		   u
			t
			 e
			  r
			 (
			r
		   o
		  u
		 t
		e
	   r
	  s
	 .
	D
	
3) A professor has exported the results of the last test from their gradebook
software. The file is of the form

    Test Name
	Test Date
	Student 1 Full Name
	Student 1 Student ID
	Student 1 Numeric Grade
	Student 2 Full Name
	Student 2 Student ID
	Student 2 Numeric Grade
	...
	
For example,

    Calculus test 1
	March 1, 2014
	Joe McCullough
	0035354422
	89
	John Greenwald
	0028834421
	93
	Lee Harrison
	0053429989
	98
	
Create a program that will prompt the user to enter the path of the results
file. If the path begins with "http://", then the program should assume the
user has specified the url of the results file. If the path does not begin with
"http://", the program should assume the file exists on the computer and
retrieve the file accordingly.

(NOTE: You can create an example file at www.pastebin.com, and click the "RAW"
tag to get the correct URL). 

The program should print the average test score. Additionally, the program
should print out the top grade and the name of the student(s) who scored it.

The user should be given the option to save this information to a local file.

4) Observe the following Python file:

	import urllib2
	import json

	def get_geo_data():
		resp = urllib2.urlopen('http://freegeoip.net/json/')
		data = json.load(resp)   
		return data

	def get_weather_info(latiude, longitude):
		base_url = "https://api.forecast.io/forecast"
		API_KEY = "cc849413324b099ad551c0a3dd9b0d32"
		url = "%s/%s/%s,%s" % (base_url, API_KEY, latiude, longitude)
		resp = urllib2.urlopen(url)
		data = json.load(resp)
		currently = data['currently']
		return "%sF: %s" % (int(currently['temperature']), currently['summary'])

The file defines two functions: get_geo_data() returns information about the
computer's current location based on its IP address. The information is in the
form of a dictionary. Here is an example return value from the function:

	{
		'city': 'Tyler',
		'region_code': 'TX',
		'region_name': 'Texas',
		'area_code': '903',
		'zipcode': '75708',
		'longitude': -95.2056,
		'metro_code': '709',
		'latitude': 32.4218,
		'country_code': 'US',
		'country_name': 'United States'
	}
	
The get_weather_info function takes latitude and longitude arguments, and
returns a string that states the current temperature and a short summary of the
weather conditions for the area containing the provided latitude/longitude. Here
is an example return value from the function:

    75F: Partly Cloudy

Use these functions to write a program which prints the name of the
City and State the computer is (estimated) to be in, along with the current
weather info.
