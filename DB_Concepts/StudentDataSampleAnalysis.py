import pymysql
import os
import csv
myDBConnectObject = pymysql.connect('127.0.0.1','test','test123','scet-autonomous')
myCursorObject = myDBConnectObject.cursor()

csvFilename = input('Enter a CSV FileName to be created with the analysis result set:')
delimiter = ','

query = "select count(*) from SCETDATASETTABLE"
myCursorObject.execute(query)
totalStudents = myCursorObject.fetchone()
print(totalStudents)
print(totalStudents[0])


query = "select count(*) from SCETDATASETTABLE where student_department = 'CSE'"
myCursorObject.execute(query)
CSEStudents = myCursorObject.fetchone()
print(CSEStudents)
print(CSEStudents[0])

query = "select count(*) from SCETDATASETTABLE where student_department = 'ECE'"
myCursorObject.execute(query)
ECEStudents = myCursorObject.fetchone()
print(ECEStudents)
print(ECEStudents[0])

query = "select count(*) from SCETDATASETTABLE where student_department = 'EEE'"
myCursorObject.execute(query)
EEEStudents = myCursorObject.fetchone()
print(EEEStudents)
print(EEEStudents[0])

query = "select count(*) from SCETDATASETTABLE where student_department = 'EIE'"
myCursorObject.execute(query)
EIEStudents = myCursorObject.fetchone()
print(EIEStudents)
print(EIEStudents[0])

query = "select count(*) from SCETDATASETTABLE where student_department = 'Civil'"
myCursorObject.execute(query)
CivilStudents = myCursorObject.fetchone()
print(CivilStudents)
print(CivilStudents[0])

query = "select count(*) from SCETDATASETTABLE where student_department = 'Mechanical'"
myCursorObject.execute(query)
MechanicalStudents = myCursorObject.fetchone()
print(MechanicalStudents)
print(MechanicalStudents[0])

fileExists = os.path.isfile(csvFilename)
with open(csvFilename,'a',newline='') as appendInToCSVFile:
	csvHeader = ['Total_Students','CSE-Total','ECE-Total','EEE-Total','EIE-Total','Civil-Total','Mechanical-Total']
	writeHeader = csv.DictWriter(appendInToCSVFile,fieldnames=csvHeader)
	if not fileExists:
		writeHeader.writeheader()
	
	appendInToCSVFile.write(str(totalStudents[0]))
	appendInToCSVFile.write(delimiter)
	appendInToCSVFile.write(str(CSEStudents[0]))
	appendInToCSVFile.write(delimiter)
	appendInToCSVFile.write(str(ECEStudents[0]))
	appendInToCSVFile.write(delimiter)
	appendInToCSVFile.write(str(EEEStudents[0]))
	appendInToCSVFile.write(delimiter)
	appendInToCSVFile.write(str(EIEStudents[0]))
	appendInToCSVFile.write(delimiter)
	appendInToCSVFile.write(str(CivilStudents[0]))
	appendInToCSVFile.write(delimiter)
	appendInToCSVFile.write(str(MechanicalStudents[0]))
	appendInToCSVFile.write('\n')
