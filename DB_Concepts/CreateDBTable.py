

import pymysql
myDBConnectObject = pymysql.connect('127.0.0.1','test','test123','scet-autonomous')
myCursorObject = myDBConnectObject.cursor()
myCreateTableQuery = 'create table FacultyTable (ID integer primary key, Name varchar(30), Designation varchar(30))'
myCursorObject.execute(myCreateTableQuery)
myDBConnectObject.close()

