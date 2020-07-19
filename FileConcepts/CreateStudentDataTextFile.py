import os
import StudentDataModule
import FileWriting

myTextFile = input('Enter the text file name to be created: ')
fileExists = os.path.isfile(myTextFile)
if not fileExists:
	myHeaderData = 'RegNo,Name,Gender,Department,CGPA,Email,Contact'
	fileWriteObject = open(myTextFile,'w')
	fileWriteObject.write(myHeaderData)
	fileWriteObject.write('\n')
	fileWriteObject.close()

regNo = 20181001
while(regNo <=20185000):
	name,gender,department,cgpa,email,contact = StudentDataModule.GetStudentDetails(regNo)
	FileWriting.FileWritingFunction(myTextFile,regNo,name,gender,department,cgpa,email,contact)
	regNo+=1

			

