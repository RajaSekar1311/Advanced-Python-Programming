import os
import csv
import time

myCSVFileName = input('Enter a CSV Filename to read its contents: ')
fileExists = os.path.isfile(myCSVFileName)
if (fileExists):
	print(myCSVFileName, 'exists')
	
	recordsList = []#Creates a empty list called as recordsList
	print(recordsList)#Prints Empty List
	with open(myCSVFileName,'r') as csvFileObject:#open a file in read mode, and execute line 13 -19
		myDictReader = csv.DictReader(csvFileObject)#Reading the contents in the form of Dictionary
		print(myDictReader)
		for eachLine in myDictReader:
			print(eachLine)
			print('\n')
			recordsList.append(eachLine)
			time.sleep(1)
		print(recordsList)
			
else:
	print(myCSVFileName,' does not exist')
	