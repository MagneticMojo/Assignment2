#!/usr/bin/env python

import sys

# initialize variables
current_word = None
current_count = 0
word = None

# input comes from STDIN (standard input)
for line in sys.stdin:
	
	# remove trailing spaces at the end of each line
	line = line.strip()

	# parse the input we got from mapper.py and store as word and count variables
	# TODO [FIX ME!]

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number,
		# so silently ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
	else:
		if current_word:
			# write result to STDOUT: key <tab> value
			# TODO [FIX ME!]

		current_count = count
		current_word = word

# do not forget to output the last word if needed!
if current_word == word:
	# write result to STDOUT: key <tab> value
    # TODO [FIX ME!]