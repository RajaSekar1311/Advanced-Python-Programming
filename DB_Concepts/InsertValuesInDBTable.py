import pymysql

myDBConnectObject = pymysql.connect('127.0.0.1','test','test123','scet-autonomous')

myCursorObject = myDBConnectObject.cursor()

myCreateTableQuery = 'create table FacultyTable (ID integer primary key, Name varchar(30), Designation varchar(30))'

myCursorObject.execute(myCreateTableQuery)

myInsertQuery = '''insert into FacultyTable (ID,Name,Designation) 
                values 
				('50301','Dr.Suresh','Assistant Professor')'''
myCursorObject.execute(myInsertQuery)

myInsertQuery = '''insert into FacultyTable (ID,Name,Designation) 
                values 
				('50302','Dr.Uday','Assistant Professor')'''
myCursorObject.execute(myInsertQuery)

myInsertQuery = '''insert into FacultyTable (ID,Name,Designation) 
                values 
				('50303','Dr.D.Ganga','Assistant Professor')'''

myCursorObject.execute(myInsertQuery)

myDBConnectObject.commit()

myDBConnectObject.close()