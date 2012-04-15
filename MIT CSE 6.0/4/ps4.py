# Problem Set 4
# Name: Shriram Kunchanapalli
# Collaborators: N/A
# Time: 

#
# Problem 1
#
from string import *

def nestEggFixed(salary, save, growthRate, years):
	"""
	- salary: the amount of money you make each year.
	- save: the percent of your salary to save in the investment account each
	  year (an integer between 0 and 100).
	- growthRate: the annual percent increase in your investment account (an
	  integer between 0 and 100).
	- years: the number of years to work.
	- return: a list whose values are the size of your retirement account at
	  the end of each year.
	"""
	newList =[]
	for i in range(years):
		newList.append(0)
	for i in range(years):
		if i == 0:
			newList[0] = salary*save*0.01
		else:
			newList[i] = newList[i-1]*(1+0.01*growthRate)+salary*save*0.01
	return newList

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
# TODO: Your code here.
	"""
	- salary: the amount of money you make each year.
	- save: the percent of your salary to save in the investment account each
	  year (an integer between 0 and 100).
	- growthRate: a list of the annual percent increases in your investment
	  account (integers between 0 and 100).
	- return: a list of your retirement account value at the end of each year.
	"""
	newList =[]
	for i in growthRates:
		newList.append(0)
	cnt = 0
	for i in growthRates:
		if cnt == 0:
			newList[0] = salary*save*0.01
		else:
			newList[cnt] = newList[cnt-1]*(1+0.01*i)+salary*save*0.01
		cnt += 1
	return newList	

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
	"""
	- savings: the initial amount of money in your savings account.
	- growthRate: a list of the annual percent increases in your investment
	  account (an integer between 0 and 100).
	- expenses: the amount of money you plan to spend each year during
	  retirement.
	- return: a list of your retirement account value at the end of each year.
	"""
	# TODO: Your code here.
	newList = []
	for i in growthRates:
		newList.append(0)
	cnt = 0
	for i in growthRates:
		if cnt == 0:
			newList[0] = savings*(1+0.01*i)-expenses;
		else:
			newList[cnt] = newList[cnt-1]*(1+0.01*i)-expenses;
		cnt += 1
	return newList

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def recurseFunc( low, high, postRetireGrowthRates, savings, epsilon ):
	expenses = (low+high)/2
	print 'low ',low,' high ', high,' expenses ', expenses	
	print 'Current estimate of expenses ', expenses
	rem = postRetirement(savings, postRetireGrowthRates, expenses )
	print 'Rem ', rem[len(rem)-1]
	val = rem[len(rem)-1]
	if( abs(val) >= 0 and abs(val) < epsilon ):
		return expenses
	elif( val < 0 ):
		expenses = recurseFunc( low, expenses, postRetireGrowthRates, savings, epsilon)
	elif( val >= epsilon ):
		expenses = recurseFunc( expenses, high, postRetireGrowthRates, savings, epsilon )
	return expenses

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
	"""
	- salary: the amount of money you make each year.
	- save: the percent of your salary to save in the investment account each 
	  year (an integer between 0 and 100).
	- preRetireGrowthRates: a list of annual growth percentages on investments
	  while you are still working.
	- postRetireGrowthRates: a list of annual growth percentages on investments
	  while you are retired.
	- epsilon: an upper bound on the absolute value of the amount remaining in
	  the investment fund at the end of retirement.
	"""
    # TODO: Your code here.
	preRetSav = nestEggVariable(salary, save, preRetireGrowthRates)
	savings = preRetSav[len(preRetSav)-1]
	#print 'Savings + epsilon ', savings+epsilon
	val = savings + epsilon + 1
	answer = recurseFunc( 0, val, postRetireGrowthRates, savings, epsilon )
	return answer

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986
	# got an answer of 1229.95528606
    # TODO: Add more test cases here.

if __name__ == '__main__':
	testNestEggFixed()
	testNestEggVariable()
	testPostRetirement()
	testFindMaxExpenses()