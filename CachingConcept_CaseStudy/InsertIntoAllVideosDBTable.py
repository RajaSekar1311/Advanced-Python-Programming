import pymysql

#open the database connection
myDBConnectObject = pymysql.connect("127.0.0.1","test","test123","scet-autonomous")

#prepare a cursor object using cursor() method
myCursorObject = myDBConnectObject.cursor()

#create a table AllVideosDBTable if it does not exist
myCreateQuery = """CREATE TABLE ALLVIDEOSDBTABLE 
				(VIDEO_ID INTEGER PRIMARY KEY,
				 VIDEO_NAME VARCHAR(50), 
				 VIDEO_LOCATION VARCHAR(100))"""
myCursorObject.execute(myCreateQuery)

#prepare myInsertQuery query to insert the video in the database
myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10001,'Video1.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10002,'Video2.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10003,'Video3.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10004,'Video4.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10005,'Video5.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10006,'Video6.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10007,'Video7.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10008,'Video8.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10009,'Video9.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10010,'Video10.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10011,'Video11.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)


myInsertQuery = """INSERT INTO ALLVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION) VALUES (10012,'Video12.avi','F:/SCET_Autonomous/Videos')""" 
myCursorObject.execute(myInsertQuery)

myDBConnectObject.commit()
myDBConnectObject.close()