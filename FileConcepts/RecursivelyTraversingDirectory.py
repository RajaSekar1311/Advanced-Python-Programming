import glob
import os
import time

DirList = []
FileNameList = []
for filesList in glob.glob("F:\SCET-Autonomous\**\*.txt", recursive=True):
	#print(filesList)
	folderPath = os.path.dirname(filesList)
	DirList.append(folderPath)
	#print("the folder path is:  "+folderPath)
	fileName = os.path.basename(filesList)
	FileNameList.append(fileName)
	#print("the filename is: "+fileName)
	#time.sleep(1)

for directory in DirList:
	print(directory)
for fname in FileNameList:
	print(fname)
	