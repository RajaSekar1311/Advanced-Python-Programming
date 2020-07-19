import pymysql

#open the database connection
myDBConnectObject = pymysql.connect("127.0.0.1","test","test123","scet-autonomous")

#prepare a cursor object using cursor() method
myCursorObject = myDBConnectObject.cursor()

#create a table CacheVideosDBTableif if does not exist
myCreateQuery = """CREATE TABLE IF NOT EXISTS CACHEVIDEOSDBTABLE
				(VIDEO_ID INTEGER PRIMARY KEY, 
				 VIDEO_NAME VARCHAR(50),
				 VIDEO_LOCATION VARCHAR(100),
				 COUNT INTEGER,
				 ACCESSED_TIMESTAMP DATETIME
				 )"""
				 
myCursorObject.execute(myCreateQuery)

myDBConnectObject.commit()

myDBConnectObject.close()