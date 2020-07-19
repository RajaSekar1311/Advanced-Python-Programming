import csv
import os
import random
import names
delimiter = ','

myCSVFileName = input('Enter a CSV Filename: ')

fileExists = os.path.isfile(myCSVFileName)

#Open the CSV File in append mode for creating the header when file does not exist, 

with open(myCSVFileName,'a',newline='') as appendInToCSVFile:
	csvHeader = ['REGISTRATION_NUMBER','STUDENT_NAME','STUDENT_GENDER','STUDENT_DEPARTMENT','STUDENT_CGPA','STUDENT_EMAILID','STUDENT_CONTACT_NUMBER']
	MyHeader = csv.DictWriter(appendInToCSVFile,fieldnames=csvHeader)
	print(MyHeader)
	if not fileExists:
		MyHeader.writeheader()

	ID = 1
	while (ID <= 3):
		studentId = ID
		appendInToCSVFile.write(str(studentId))
		appendInToCSVFile.write(delimiter)
		firstName = names.get_first_name()
		lastName = names.get_last_name()
		studentName = firstName+' '+lastName
		appendInToCSVFile.write(studentName)
		appendInToCSVFile.write(delimiter)
		studentGender = random.choice(['Male','Female'])
		appendInToCSVFile.write(studentGender)
		appendInToCSVFile.write(delimiter)
		studentDepartment = random.choice(['CSE','ECE','EEE','Mechanical','Civil','EIE'])
		appendInToCSVFile.write(studentDepartment)
		appendInToCSVFile.write(delimiter)
		studentCGPA = round((random.uniform(5.00,10.00)),2)
		appendInToCSVFile.write(str(studentCGPA))
		appendInToCSVFile.write(delimiter)
		emailTag = random.choice(['@gmail.com','@yahoo.co.in','@rediffmail.com','@hotmail.com'])
		studentEmailId = firstName+lastName+emailTag
		appendInToCSVFile.write(studentEmailId)
		appendInToCSVFile.write(delimiter)
		studentContactNum = random.randint(9986000000,9986999999)
		appendInToCSVFile.write(str(studentContactNum))
		appendInToCSVFile.write('\n')
		ID+=1