import pymysql
import csv
import os


myCSVFileName= input('Enter a Filename: ')
fileExists = os.path.isfile(myCSVFileName)

myDBConnectObject = pymysql.connect('127.0.0.1','test','test123','scet-autonomous')

if fileExists:
	print(myCSVFileName,' exist to load in to the Database Table')
	
	myCursorObject = myDBConnectObject.cursor()

	createTableQuery = 'create table if not exists SCETDATASETTABLE (REGISTRATION_NUMBER bigint,STUDENT_NAME varchar(50),STUDENT_GENDER VARCHAR(20),STUDENT_DEPARTMENT VARCHAR(20),STUDENT_CGPA float(4,2),STUDENT_EMAILID varchar(50), STUDENT_CONTACT_NUMBER bigint)'
	myCursorObject.execute(createTableQuery)

	record = []
	with open(myCSVFileName,'r') as csvFileObject:
		reader = csv.DictReader(csvFileObject)
		for line in reader:
			record.append(line)
		

		for i in range(0,5000):
			Col1 = record[i]['REGISTRATION_NUMBER']
			Col2 = record[i]['STUDENT_NAME']
			Col3 = record[i]['STUDENT_GENDER']
			Col4 = record[i]['STUDENT_DEPARTMENT']
			Col5 = record[i]['STUDENT_CGPA']
			Col6 = record[i]['STUDENT_EMAILID']
			Col7 = record[i]['STUDENT_CONTACT_NUMBER']
			insertQuery = "INSERT INTO SCETDATASETTABLE (REGISTRATION_NUMBER, STUDENT_NAME, STUDENT_GENDER,STUDENT_DEPARTMENT,STUDENT_CGPA,STUDENT_EMAILID, STUDENT_CONTACT_NUMBER) VALUES('%s','%s','%s','%s','%s','%s','%s')"%(Col1,Col2,Col3,Col4,Col5,Col6,Col7)
			myCursorObject.execute(insertQuery)
else:
	print(myCSVFileName,' does not exist to load in to the Database Table')

myDBConnectObject.commit()
myDBConnectObject.close()
