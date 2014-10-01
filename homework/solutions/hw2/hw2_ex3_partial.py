'''
3) A professor has exported the results of the last test from their gradebook software. The file is of the form

Test Name
Test Date
Student 1 Full Name
Student 1 Student ID
Student 1 Numeric Grade
Student 2 Full Name
Student 2 Student ID
Student 2 Numeric Grade
...

'''

import urllib2

# 1. check if it's a file or a URL
def is_url(txt):
	return txt.startswith('http://') or txt.startswith('https://')

# 2. if URL, read from the web URL
# 3. otherwise, read the data from a file
def get_data(filename):
	if is_url(filename):
		txt = urllib2.urlopen(filename).read()
	else:
		with open(filename) as f:
			txt = f.read()
	return txt.replace('\r','') # normalize PC/Windows newlines \r\n => \n

# 4. The program should print the average test score.
# 5. The program should print out the top grade and the name of the student(s) who scored it.
# 6. The user should be given the option to save this information to a local file.
def analyze_data(data): # input raw data from the file
	lines = data.split('\n')
	test_scores = lines[4::3]
	test_scores = [int(x) for x in test_scores] # the scores are strings, gotta convert to ints:	
	avg_score = 1.0 * sum(test_scores) / len(test_scores)
	print 'Average test score =', avg_score

data = get_data('http://pastebin.com/raw.php?i=mWTWm7Ly')
analyze_data(data)
