import os
import time
#providing the path of the directory
directorypath = 'F:\SCET-Autonomous\Videos'

#Displaying all the available video files which will be randomly selected in the program execution
print('\nListing all the available video files for selection...')
#To display all the available video files with the extension avi
filesList = [file for file in os.listdir(directorypath) if file.endswith(".avi")]
print(filesList)

for file in filesList:
		print(os.path.join(directorypath,file))
		time.sleep(1)
