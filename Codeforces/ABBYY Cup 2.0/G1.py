#http://codeforces.com/contest/177/problem/G1
#Fibonacci Numbers
val = raw_input()
li = val.split()

str1 = "a"
str2 = "b"
if int(li[0]) == 1:
	str2 = "a"
elif int(li[0]) == 2:
	str2 = "b"
else:
	cnt = 2 
	while cnt < int(li[0]):
		temp = str2
		str2 += str1
		str1 = temp
		cnt += 1
print 'str ', str2
val = (1000000007*(10**9+7))
for i in range(int(li[1])):
    testStr = raw_input()
    #print 'testStr ', testStr
    fChar = testStr[0]
    listOfPos = []
    for pos in range(len(str2)):
        if str2[pos] == fChar:
            listOfPos.append(pos)
    if testStr in str2:
        count = 0
        for j in listOfPos:		
		#for j in range(0, len(str2) - len(testStr) + 1):
			#if str2[j:j+1] == testStr[:1] and str2[j:len(testStr)+j] == testStr:
			if str2[j:len(testStr)+j] == testStr:
				count += 1
				count %= val
        print count
    else:
		print 0
		
/******
[08:44] <Mavericks> hello folks , what's the best way to construct and store a fibonacci string as explained @ http://codeforces.com/contest/177/problem/G1 of length 3000 ?
[08:45] <Mavericks> i did it brute force way and get a memory error
[08:45] <Mavericks> https://gist.github.com/2605279
[08:45] <Mavericks> any hint?
[08:56] <R_G> Mavericks: if source code length isn't a problem, just hardcode it
[08:57] <R_G> also, note the relation between each successive string and how you can use that to limit what you need to hardcode
[08:58] <hua> R_G they are asking for up to the 10^18th string
[08:58] <hua> i dont think that is hardcodable ;d
[08:58] <R_G> he said the length of 3k one
[08:58] <R_G> I'm not talking about the 10^18
[08:58] <hua> oh right
[08:58] <hua> yeah i would just hardcode that good call.
[08:58] <hua> if you can, it wouldnt work on spoj for example
[08:58] <R_G> also, in regards to the problem, I think the right approach has to do with the patterns in the string rather than searching
[08:58] <hua> still too big
[08:59] <R_G> since searching for a substring in a string of 3k can take n^2 time
[08:59] <R_G> and you have n searches to do, potentially
[08:59] <R_G> so worst case n^3 on 3k isn't really viable
[09:00] <R_G> I guess if string.count in Python uses KMP, it would go down to n^2logn
[09:00] <R_G> but that approach would only work for the small, and only if the constants were small enough
[09:03] <hua> hmm one of the solutions uses the fibonacci number matrix
[09:03] <R_G> that sounds slow
[09:03] <hua> ?
[09:03] <R_G> well, nvm
[09:03] <hua> the 2x2 matrix you use to calculate big fibonacci numbers
[09:03] <R_G> no, I know
[09:03] <hua> except it's 20 by 20
[09:03] <hua> and has 2 matrices
[09:03] <hua> i dont know whats going on =\
[09:03] <R_G> huh
[09:04] <R_G> I was about to say:
[09:04] <hua> the moral of this story is don't be tricked by the contest being called "easy" the problem is incredibly difficult
[09:04] <R_G> also also, since the solution can potentially be over 1 billion, counting the number of occurrences will probably TLE
[09:04] <R_G> no matter how good count may be, it can't have a complexity of better than n
[09:04] <hua> ok another guy uses the classic 2x2 matric
[09:05] <hua> unfortunately no one has been taught how to name variables on codeforces
[09:05] <R_G> no, they've been taught very well
[09:05] <R_G> I should write a code obfuscater
[09:05] <R_G> so I can name my variables well and then obfuscate them in a second
[09:14] <Mavericks> R_G: sorry i just got your message a few minutes ago.
[09:15] <Mavericks> R_G: sorry I mean the 3000th fibonacci string than the string of length 3000. sorryfor the confusion
[09:16] <Mavericks> hua: yes, i learnt it the hard way
[09:16] <Mavericks> it's not at all easy. well for me at this moment
[09:17] <R_G> I see what's going on
[09:17] <R_G> I see how the fibonacci matrix would help here
[09:17] <Mavericks> hua: lol - > naming variables. i wonder that's how they re taught to do to make for lost time/speed or thye are just lazy.
[09:18] <R_G> for example, for "a" and "b", the answer would just be the fibonacci number at index k for the sequence starting with (1, 0) and (0, 1)
[09:19] <R_G> which is interesting, because it's the same as the fibonacci number at index k-1 and k, respectively
[09:19] <R_G> but for others, I think it just might be the fibonacci numbers shifted by some index
[09:19] <Mavericks> R_G: how does searching for a substring in string of 3k take n^2 time
[09:19] <R_G> Mavericks: think about it
[09:19] <R_G> this is something you should thoroughly understand, since it is a fundamental interview question
[09:20] <Mavericks> string of length n ,
[09:20] <R_G> it looks like this problem would ultimately boil down to figuring out how much to shift the fibonacci number index, and quickly calculating the fibonacci number at a particular inde
[09:20] <R_G> which is why it's solvable for 10^18
[09:21] <R_G> brute forcing it might expose the pattern, but I'm lazy and pretty sure I figured out most of the problem
[09:21] <R_G> Mavericks: string is of length n
[09:21] <R_G> substring of length k
[09:21] <R_G> in actuality, the search can take a max of n*k
[09:22] <Mavericks> i'm looking at this picture
[09:22] <Mavericks> http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/kmpen.htm
[09:22] <Mavericks> at the bottom it says 2n comparisons atm
[09:22] <R_G> Mavericks: you're looking at KMP
[09:23] <R_G> which has max of nlogn
[09:23] <Mavericks> ok
[09:23] <R_G> the brute force way of doing it has n*k comparisons
[09:23] <Mavericks> aaah!
[09:23] <Mavericks> kk
[09:23] <R_G> and if k == n, it has roughly n^2 comparisons
[09:23] <Mavericks> yes! facepalm
[09:24] <R_G> still, n^2logn for n=3k is fine, but with high constants, you'd probably TLE
[09:24] <R_G> that's not even considering the fact that n is actually much larger
[09:24] <R_G> for 3k, the string is of length Fibonacci(3000)
[09:24] <Mavericks> now your statement on n^3 makes sense  too
[09:25] <R_G> which is: 4 x 10^626
[09:25] <R_G> that's not even storable or searchable
[09:25] <Mavericks> yeah!
[09:25] <R_G> so forget generating the string
[09:25] <R_G> impossible
[09:25] <R_G> brute force won't work for anything larger than n = 100 or something
[09:25] <Mavericks> trying it now
[09:26] <R_G> yeah, even that is too much
[09:26] <Mavericks> yea it's hanging out there on screen blinking. waiting for system to interrupt  ok
[09:26] <R_G> basically, your max case is n*FlogF, where n is the max from the problem and F is the fibonacci number at index n
[09:28] <R_G> and if n is even 50, that number comes to 10^13
[09:30] <Mavericks> was it 10^626 or 10^6
[09:31] <R_G> 10^626
[09:31] <R_G> at the end of the day, your brute force will only terminate for something where the limits are less than 35 or so
[09:32] <R_G> well, terminate as in not TLE
[09:32] <R_G> so you need to think about the problem more
[09:32] <R_G> well, good night
[09:32] <R_G> gotta wake up early tomorrow
[09:32] <Mavericks> which's true. i'm still pondering about the 10^626
[09:32] <Mavericks> thanks again
[09:32] <R_G> hf Codeforcing
[09:32] <R_G> Mavericks: think about the length of the kth string
[09:32] <R_G> you'll figure out where I got that number
[09:32] <Mavericks> yes but i'mlooking at n^2logn
[09:33] <R_G> don't.
[09:33] <R_G> that's not where
[09:33] <R_G> ignore the n^2logn
[09:33] <R_G> that complexity is wrong
[09:33] <Mavericks> ok will do that
[09:33] <R_G> the real complexity is n*Fib(n)*log(Fib(n))
[09:33] <Mavericks> oh!
[09:33] <R_G> Fib(3000) = 4x10^626
[09:33] <R_G> that's where
[09:34] <R_G> see if you can figure out how I got to that conclusion, though
[09:34] <Mavericks> that's why you wrote the string is of length Fibonacci(3000)
[09:34] <R_G> yeah
[09:34] <Mavericks> yeah the real coomplexity makes sense
[09:35] <Mavericks> really is that . aah 35 or so for limit make sense too
[09:35] <Mavericks> i totally underestimated this problem
***************/