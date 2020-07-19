#Searching an existence of a file in Current directory
import os
#myFileName = 'UnderstandLists.py'
#isfile() returns a boolean value True if file is available
#isfile() returns a boolean value False if file is not available
#fileExists = os.path.isfile(myFileName)
#print(fileExists)
myFileName = input('Enter a File Name to search:  ')
fileExists = os.path.isfile(myFileName)

if(fileExists):
	print(myFileName, 'is available')
else:
	print(myFileName, 'is not available')



