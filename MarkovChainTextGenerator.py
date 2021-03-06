#! -*- coding: UTF-8 -*-

import re, random

text = open("text.txt", "r").read()

# This dict will be hold our 'word's and their possible letters.
words = {}

wordWide = 4			# Example 'word' length. Higher values generates more meaningful results.
generateLimit = 1500	# Generate limit.

# Extract example words from text.
for i in range(0, len(text)-wordWide):
	# If it is already in dict, then add next letter to it.
	if text[i:i+wordWide] in words:
		words[text[i:i+wordWide]].append(text[i+wordWide])
		
	# If it isn't already in dict, then add example 'word' and next letter.
	else:
		words.update({
				text[i:i+wordWide]:[text[i+wordWide]]
			}
		)

# Select random seed from extracted examples.
rs = random.randint(0, len(words)-1)
seed = list(words.keys())[rs]
print("Seed: " + str(seed))

generated = seed
curWide = seed

# Generate text.
while curWide in words:
	possibleLetters = words[curWide]		# Take current generated 'word'.
	
	ri = random.randint(0, len(possibleLetters)-1)		# Choose a letter from that word's letter list randomly*.
	
	# *Not completely random actually.
	# It is possible to have any letter duplicated in that list.
	# If it is in multiple times in list, more chance it gets.
	 
	nextLetter = possibleLetters[ri]	# Get the letter.
	
	generated += nextLetter				# Concatenate letter with generated text.
	curWide = generated[-wordWide:]		# Next 'word' comes from last generated text.
	
	# Limit control.
	if len(generated) > generateLimit:
		break

print(generated)

# Write generated text to file.
out = open("out.txt", "w")
out.write(generated)
out.close()
