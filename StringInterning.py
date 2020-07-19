'''
#Example for String interning in python
string1 = 'Nagaraju'
print('String 1 is:',string1 ,'and its ID is',id(string1))
string2 = 'nagaraju'
print('String 2 is:',string2 ,'and its ID is',id(string2))
string3 = 'Nagaraju'
print('String 3 is:',string3 ,'and its ID is',id(string3))
string4 = 'nagaraju'
print('String 4 is:',string4 ,'and its ID is',id(string4))
'''
#Multiple Line Comments are written as ''', '''
import time
#Example to show the comparison of String comparision with the String's Indetity comparison
def compare_with_equality_operator(n):
	string1 = 'Python_Programming'*5000
	string2 = 'Python_Programming'*5000
	for i in range(n):
		if string1 == string2:
			pass
def compare_identity_with_IS_operator(n):
	string1 = 'Python_Programming'*5000
	string2 = 'Python_Programming'*5000
	for i in range(n):
		if string1 is string2:
			pass
startTime = time.time()
compare_with_equality_operator(100000)
endTime = time.time()
totalTime = endTime - startTime
print('Total Time Taken by comparision with equality is:   ',totalTime)

startTime = time.time()
compare_identity_with_IS_operator(100000)
endTime = time.time()
totalTime = endTime - startTime
print('Total Time Taken by comparision with identity is:   ',totalTime)




