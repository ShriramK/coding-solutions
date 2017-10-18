# 6.00 Problem Set 6
#
# The 6.00 Word Game
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

points_dict = None
time_limit = None
rearrange_dict = None

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in in_file:
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
        freq[x] = freq.get(x, 0) + 1
    return freq
"""
def generate_permutations(value, list_of_chars):
	# print 'list_of_chars in generate_permutations loop', list_of_chars,'type '
	# print type(list_of_chars)
	num_of_chars = value
	allowed_chars = []
	for i in list_of_chars:
		allowed_chars.append(i)
	# print 'allowed_chars ', allowed_chars
	status = []
	for tmp in range(num_of_chars):
		status.append(0)

	last_char = len(allowed_chars)

	rows = []
	for x in xrange(last_char ** num_of_chars):
		rows.append("")
		for y in range(num_of_chars - 1, -1, -1):
			key = status[y]
			rows[x] = allowed_chars[key] + rows[x]
		for pos in range(num_of_chars - 1, -1, -1):
			if status[pos] == last_char - 1:
				status[pos] = 0
			else:
				status[pos] += 1
				break
	# print 'rows ', rows
	return rows

def get_subsets(list_of_chars):
	li = []
	# print 'list_of_chars ', list_of_chars
	# print 'len(list_of_chars) ' + str(len(list_of_chars))
	for i in range(len(list_of_chars) + 1):
		# print len(generate_permutations(i))
		if i != 0:
			li += generate_permutations(i, list_of_chars)
			# print 'list ', list
	return li
"""

def choose_iter(elements, length):
    new_len = length - 1
    for i in xrange(len(elements)):
        if length == 1:
            yield (elements[i], )
        else:
            for next in choose_iter(elements[i + 1: len(elements)], new_len):
                yield (elements[i], ) + next

def choose(l, k):
    return list(choose_iter(l, k))

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
    if len(word) == n:
        score += 50
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a': 1, 'x': 2, 'l': 3, 'e': 1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    freq = get_frequency_dict(word)
    newhand = {}
    for char in hand:
        newhand[char] = hand[char] - freq.get(char, 0)
    return newhand
    # return dict((c, hand[c] - freq.get(c, 0)) for c in hand)
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
	# print 'points_dict type', type(points_dict)
    return points_dict.get(word, 0) > 0 # word in word_list

def pick_best_word(hand, points_dict):
	"""
	Return the highest scoring word from points_dict that can be made with
	the given hand.	Return '.' if no words can be made with the given hand.
	"""
	ans = '.'
	print hand 
	for word in points_dict.keys():
		freq = get_frequency_dict(word)
		con = False
		for letter in word:
			if freq[letter] > hand.get(letter, 0):
				con = True
				break
		if not con:
			if ans == '.':
				ans = word
			elif points_dict[word] > points_dict[ans]:
				ans = word
	return ans

def pick_best_word_faster(hand, rearrange_dict):
	list_of_chars = []
	for i in hand.keys():
		for j in range(hand[i]):
			list_of_chars += i
	print 'list_of_chars ', list_of_chars
	li = list_of_chars
	res = []
	for i in range(len(li) + 1):  # word) + 1):
		# res += list(set(choose(li, i)))
		ans = []
		for e in choose(li, i):
			if e not in ans:
				ans.append("".join(e))
		res += ans
		print list(set(choose(li, i)))
	print 'Value of res ', res
	word_combinations = res  # get_subsets(res)# li)# get_subsets
	max_score = -1
	score = 0
	ans = None
	sorted_word_subset = None
	for word_subset in word_combinations:
		# print 'word_subset ', word_subset
		sorted_word_subset = "".join(sorted(word_subset))
		# print 'sorted_word_subset ', sorted_word_subset
		if sorted_word_subset in rearrange_dict:
			# print 'Found again', sorted_word_subset, word_subset
			# print 'rearrange-dict ', rearrange_dict
			word = rearrange_dict[sorted_word_subset]
			print 'Word ', word
			score = points_dict[word]
			if score > max_score:
				max_score = score
				ans = word
	if ans is not None:
		return ans
	else:
		return '.'

def get_time_limit(points_dict, k):
	"""
	Return the time limit for the computer player as a function of the
	multiplier k. points_dict should be the same dictionary that is created
	by get_words_to_points.
	"""
	start_time = time.time()
	# Do some computation. The only purpose of the computation is so we can
	# figure out how long your computer takes to perform a known task.
	for word in points_dict:
		get_frequency_dict(word)
		get_word_score(word, HAND_SIZE)
	end_time = time.time()
	return (end_time - start_time) * k

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
	"""
	Allows the user to play the given hand, as follows:

	* The hand is displayed.

	* The user may input a word.

	* An invalid word is rejected, and a message is displayed asking
	  the user to choose another word.

	* When a valid word is entered, it uses up letters from the hand.

	* After every valid word: the score for that word is displayed,
	  the remaining letters in the hand are displayed, and the user
	  is asked to input another word.

	* The sum of the word scores is displayed when the hand finishes.

	* The hand finishes when there are no more unused letters.
	  The user can also finish playing the hand by inputing a single
	  period (the string '.') instead of a word.

	  hand: dictionary (string -> int)
	  word_list: list of lowercase strings
	"""
	total = 0
	initial_handlen = sum(hand.values())
	# time_limit = float(raw_input('Enter time limit, in seconds, for players:
	# '))
	count = time_limit  # time_limit
	# print 'Computer Time Limit ', time_limit
	while sum(hand.values()) > 0:
		print 'Current Hand:',
		display_hand(hand)
		start_time = time.time()
		# user_word = raw_input('Enter word, or a . to indicate that you are
		# finished: ')
		user_word = pick_best_word_faster(hand, rearrange_dict)  # points_dict)
		# print 'userWord ', user_word
		if user_word == '.':
			break
		else:
			end_time = time.time()
			total_time = end_time - start_time
			print 'It took %0.2f seconds to provide an answer.' % total_time
			rem = count - total_time
			if rem >= 0:
				print 'You have %0.2f seconds remaining.' % rem
				count = rem
			else:
				print 'Total time exceeds %0.2f seconds. You scored %0.2f '\
						'points.' % (time_limit, total)
				break
			is_valid = is_valid_word(user_word, hand, points_dict)
			# word_list)
			if not is_valid:
				print 'Invalid word, please try again.'
			else:
				points = get_word_score(user_word, initial_handlen)
				total += points
				print '%s earned %d points. Total: %d points'\
					% (user_word, points, total)
				hand = update_hand(hand, user_word)
	print 'Total score: %d points.' % total


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    hand = deal_hand(HAND_SIZE) # random init
    while True:
    	input_instruction = 'Enter n to deal a new hand, r to replay the last'
    	input_instruction += ' hand, or e to end game: '
        cmd = raw_input(input_instruction)
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

def get_words_to_points(word_list):
	"""
	Return a dict that maps every word in word_list to its point value.
	"""
	word_point_value = {}
	for word in word_list:
		score = 0
		for letter in word:
			score += SCRABBLE_LETTER_VALUES[letter]
		word_point_value[word] = score
		# print word, ' ', word_point_value[word]
	# print 'word_point_value ', type(word_point_value)
	# print 'word ', type(word)
	return word_point_value

def get_word_rearrangements(word_list):
	d = {}
	for word in word_list:
		"""
		Two ways to sort as per Sorting elements in string with
		Python - Stack Overflow
		"""
		# new_word = []
		# for letter in word:
		#	new_word.append(letter)
		# new_word.sort()
		# get/return the string with
		# "".join(new_word) - (converting a list to a string)
		sorted_word = "".join(sorted(word))
		d[sorted_word] = word
	return d

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
	word_list = load_words()
	points_dict = get_words_to_points(word_list)
	time_limit = get_time_limit(points_dict, 1)
	rearrange_dict = get_word_rearrangements(word_list)
	hand_data = {'a': 2, 'b': 2, 'd': 1, 't': 1}
	# print 'Pick best word faster',
	# print pick_best_word_faster(hand_data, rearrange_dict)
	# print time_limit
	play_game(word_list)
	# print pick_best_word({'a': 3,'b': 3,'c': 3}, points_dict)
	hand_data = {'a': 1, 'c': 1, 'f': 1, 'i': 1, 's': 1, 't': 1, 'x': 1}
	print ' Best word ', pick_best_word_faster(hand_data, rearrange_dict)
