# Create a program which continuously prompts the user
# to enter numbers until they type in a phrase of your choice.
# Calculate and print the mean, median, and mode of the numbers
# provided.

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print "Enter tons of numbers until you're sick of it, then type 'stop'."
numbers = []
while True:
	user_input = raw_input('Enter a number or "stop": ')
	if user_input.lower() == 'stop':
		print "Okay, okay!"
		break
	if is_number(user_input):
		user_input = float(user_input)
		if user_input == int(user_input): # let ints be just ints
			user_input = int(user_input)
		numbers.append(user_input)
	else:
		print "Ummmm, I think I asked you to type a number or 'stop'..."

print "Just to make sure, were those numbers", numbers, "?"

# mean, median, mode
def mean(L):
	return sum(L) / float(len(L))
def median(L):
	# once you sort all the elements in L, what's the "middle" one?
	# if there's 2 middle ones, average them
	sortedL = sorted(L)
	if len(L) % 2 == 0:
		return (sortedL[len(L) / 2] + sortedL[len(L)/2 - 1]) / 2.0
	else:
		return sortedL[len(L) / 2]
def mode(L):
	# the one that's most commonly occurring
	# if there's more than one, give a list of all of them
	counts = {} # keys are going to be the counts, and the values are which numbers have those counts
	# for example, if the list L is [5,5,3,3,2]:
	#	counts is going to be { 2: [5,3], 1: [2] } because there are 2 5's and 3's and 1 2
	for i in L: # loop through the elements in L
		if L.count(i) not in counts:
			counts[L.count(i)] = set()
		counts[L.count(i)].add(i)
	# let's walk thru the example in more detail:
	#	for i in L: we're walking through the list.  First item: 5
	#	how many 5's are there in L?  L.count(5) => 2
	#	if L.count(5) not in counts ... what's going on here?
	#	it's asking does counts have a key of 2
	#	it's saying:
	#		if 2 not in counts:
	#			counts[2] = set()
	#		so basically make an empty set if there wasn't a set there already
	#	then, we just add our element 5 to the set at counts[2]:
	#		counts[2].add(5)
	# so as an example, if we call mode([1,1,1,5,3,3,4])
	# then counts = {1: set([4, 5]), 2: set([3]), 3: set([1])}
	# now we need the maximum key within counts
	max_key = max(counts.keys())
	return counts[max_key]

print "I have news for you about those numbers you gave me!"
print "Mean =", mean(numbers)
print "Median =", median(numbers)
print "Mode =", mode(numbers)
