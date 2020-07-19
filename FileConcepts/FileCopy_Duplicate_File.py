import os
#reading the source file from the standard input device i.e., keyboard
sourceFileName = input('Enter the Source filename: ')

#verifying the existence of the source file
fileExists = os.path.isfile(sourceFileName)

if not fileExists:
	print(sourceFileName," does not exist")
else:
	#logic for creating a duplicate file name with source filename ending with string _Duplicate_File
	print(sourceFileName," is available for copying")
	tempFileName = sourceFileName.split('.')
	print(tempFileName)
	print('The filename is: ',tempFileName[0])
	print('The extension is: ',tempFileName[1])
	destinationFileName = tempFileName[0]+'_Duplicate_File.'+tempFileName[1]
	print(destinationFileName)
	#reading the source file contents through the source file object named as fileReadObject
	fileReadObject = open(sourceFileName,'r')
	sourceFileContents = fileReadObject.read()
	#writing the source file contents in to the destination duplicate file
	fileWriteObject = open(destinationFileName,'w')
	fileWriteObject.write(sourceFileContents)
	