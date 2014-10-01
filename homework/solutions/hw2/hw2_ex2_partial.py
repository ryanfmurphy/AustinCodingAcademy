'''
2) Create a program which prints each non-whitespace character of a file in a zig-zag pattern. For example, for a file that begins like^
'''

def zigzag(txt):
	# 1. get rid of all whitespace characters
	txt = txt.replace(' ','').replace('\n','').replace('\t','')
	# 2. print in a zig-zag pattern:
	#	go in a loop
	#	keep track of where we are in the zigzag
	#	keep track of direction, switch when we get to the end
	xpos = 0
	for ch in txt:
		print ' '*xpos + ch
		xpos += 1

# 3. load data from a file and zigzag() it
txt = raw_input('give me some txt: ')
zigzag(txt)
