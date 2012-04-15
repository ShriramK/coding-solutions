from ps5_ghost import *

def test_is_fragment_valid():
	"""
	Unit test for is_fragment_valid
	"""
	failure=False
	# dictionary of words with fragments and fragments
	fragments = {"":False, "it":True, "was":True, "waz":True, "scored":True, "cored":True, "waybill":True, "outgnaw":True, "outgnawn":True,"p":True,"py":True,"pyt":True,"pyth":True,"pytho":True,
"python":True,"qz":False,"pyn":False,"pear":True,"peaf":True, "peafa":False,"peafo":True,
"peafow":True,"peafowl":True}
	for fragment in fragments:
		ans = is_fragment_valid(fragment)
		#print 'fragment ', fragment, 'fragments[fragment]', fragments[fragment], ' ans ', ans
		if fragments[fragment] != ans:
			failure = True		
			print "FAILURE: test_is_fragment_valid()"
			print "\tExpected ", fragments[fragment]," but got '",ans,"' for fragment '",fragment
		if failure == True:
			break
	if not failure:
		print "SUCCESS: test_get_word_score()"	

def test_is_fragment_word():
	"""
	Unit test for is_fragment_word
	"""
	failure = False
	fragments = {"":False, "it":False, "was":False, "waz":False, "scored":True, "cored":True, "waybill":True, "outgnaw":True, "outgnawn":True,"p":False,"py":False,"pyt":False,"pyth":False,"pytho":False,
"python":True,"pear":True,"peaf":False,"peafo":False, "peafow":False,"peafowl":True}
	for fragment in fragments:
		ans = is_fragment_word(fragment)
		#print 'ans',ans
		#print 'fragment ', fragment, 'fragments[fragment]', fragments[fragment], ' ans ', ans
		if fragments[fragment] != ans:
			failure = True
			print "FAILURE: test_is_fragment_word()"
			print "\tExpected ", fragments[fragment]," but got '",ans,"' for fragment '",fragment
		if failure == True:
			break
	if not failure:
		print "SUCCESS: test_get_word_score()"
#word_list = load_words()
print "----------------------------------------------------------------------"
print "Testing is_fragment_valid..."
test_is_fragment_valid()
print "----------------------------------------------------------------------"
print "Testing is_fragment_word..."
test_is_fragment_word()
print "----------------------------------------------------------------------"
print "All done!"