# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
def ghost():
	fragment = ""
	player = 1
	opponent = 2
	print 'Player 1 goes first.'
	letter = string.lower(raw_input())
	while True:
		while True:
			if not letter in string.ascii_letters:
				print 'Invalid letter. Please enter a valid letter'
				letter = string.lower(raw_input())
			else:
				break
		fragment += letter
		print 'Current word fragment: ', fragment
		if not is_fragment_valid(fragment):#con == False: #word doesn't exist Current player loses
			print 'Player ',player,' loses because no word begins with ', fragment,'!'
			print 'Player ',opponent,' wins!'
			break
		else:
			if is_fragment_word(fragment):
				print 'Player ',player,' loses because '"'",fragment,"'"' is a word!'
				print 'Player ',opponent,' wins!'
				break
			#switch player
			if player == 2:
				player = 1
				opponent = 2
			else:
				player = 2
				opponent = 1
			print "Player ",player,"'s turn"
			letter = string.lower(raw_input())			
			print 'Player ',player,' says letter: ',letter

def is_fragment_valid(fragment):
	size = len(fragment)
	for word in wordlist:
		if size <= len(word):
			for i in range(size):
				if fragment[i] == word[i]:
					if i == size-1:
						return True
				else:
					break#no such word exists
	return False
def is_fragment_word(fragment):
	for i in wordlist:
		if fragment == i:
			if len(fragment) > 3:
				return True
	return False	
		
if __name__ == '__main__':
	print 'Welcome to Ghost!'
	while True:
		print
		cmd = raw_input('Enter y to play game , or n to end game: ')
		if cmd == 'n':
			print "Ending Ghost"
			break
		elif cmd == 'y':
			ghost()
		else:
			print "Invalid command."