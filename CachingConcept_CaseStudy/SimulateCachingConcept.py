import pymysql
import os
import random
import datetime
import time


#####Database Access Starts
#open the database connection
myDBConnectObject = pymysql.connect("127.0.0.1","test","test123","scet-autonomous")

#prepare a cursor object using cursor() method
myCursorObject = myDBConnectObject.cursor()

#providing the path of the directory
directorypath = 'F:\SCET-Autonomous\Videos'

#Displaying all the available video files which will be randomly selected in the program execution
print('\nListing all the available video files for selection...')
filesList = [file for file in os.listdir(directorypath) if file.endswith(".avi")]
print(filesList)

for file in filesList:
		print(os.path.join(directorypath,file))
		#time.sleep(1)

for i in range(1,2):
	#selecting a video file randomly from the available list of video files
	randomFile = random.choice(filesList)
	print("Randomly selected video file is :  ",randomFile)

	#fetching all the video names from the cache database table
	selectQuery = "SELECT VIDEO_NAME FROM CACHEVIDEOSDBTABLE"
	myCursorObject.execute(selectQuery)
	#checking if the cache table is empty. This will be true initially
	totalRecords = myCursorObject.rowcount
	print('The Number of Records in the Cache Table: ',totalRecords)
	if(totalRecords < 3):
		print('The Cache Table maximum entries of 3 records is not reached yet...')
		print('Pushing the contents in to the cache table without page replacement...')
		selectQuery = "SELECT * FROM ALLVIDEOSDBTABLE WHERE VIDEO_NAME = '%s' "%(randomFile)
		myCursorObject.execute(selectQuery)
		myResultSet = myCursorObject.fetchone()
		print(myResultSet)
		videoID = myResultSet[0]
		videoName = myResultSet[1]
		videoLocation = myResultSet[2]
		print(videoID)
		print(videoName)
		print(videoLocation)
		videoViewCount = 1
		videoAccessedTimeStamp = 'NULL'
		insertQuery = "INSERT INTO CACHEVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION,COUNT,ACCESSED_TIMESTAMP) VALUES ('%s','%s','%s','%s','%s')"%(videoID,videoName,videoLocation,videoViewCount,videoAccessedTimeStamp)
		myCursorObject.execute(insertQuery)
		updateQuery = "UPDATE CACHEVIDEOSDBTABLE SET ACCESSED_TIMESTAMP = CURRENT_TIMESTAMP() WHERE VIDEO_NAME = '%s' "%(randomFile)
		myCursorObject.execute(updateQuery)
		myDBConnectObject.commit()
		exit()

	cacheRecords= myCursorObject.fetchall()

	#displaying all the available videos from the cache database
	print("Listing the available video file names from the Cache Database...")
	
	for record in cacheRecords:
		print(record)
		time.sleep(1)
	
	#FETCHALL will return TUPLE, so to compare a string with tuple, create a list, add the string to the list and then verify the tuple of list with the DB record
	x = []
	x.append(randomFile)
	
	#Checking whether the randomFile which is a Video Filename is available in the CacheDBTable
	if tuple(x) in cacheRecords:
		print(randomFile+'   is available in Cache Database')
		time.sleep(2)
		
		#The moment video location is found in the CacheDBTable, then
		#The count is incremented by one which indicates the frequency of usage
		query = "UPDATE CACHEVIDEOSDBTABLE SET COUNT = COUNT + 1 WHERE VIDEO_NAME = '%s' "%(randomFile)
		myCursorObject.execute(query)
		myDBConnectObject.commit()
		
		#The moment the video is accessed from the CacheFileSystem a timestamp w.r.t. to the system time at the time of access is inserted in the Cachetable
		#Timestamp of when the record is accessed will be useful when there are multiple records with least count are fetched
		#Depending on the difference of timestamps the logic is to delete the oldest record as a Cache Replacement Policy
		accessedTimeStamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
		print('The timestamp when the record is accessed from cache is :'+accessedTimeStamp)
		query = "UPDATE CACHEVIDEOSDBTABLE SET ACCESSED_TIMESTAMP = CURRENT_TIMESTAMP() WHERE VIDEO_NAME = '%s' "%(randomFile)
		myCursorObject.execute(query)
		myDBConnectObject.commit()

		time.sleep(1)
		
	else:
		print(randomFile+'   is not available in Cache Database')
		time.sleep(1)
		
		#Getting the minimum count from the CacheVidoesDBTable, it recieves a tuple, convert it to a string
		query = "SELECT MIN(COUNT) AS LRU FROM CACHEVIDEOSDBTABLE"
		myCursorObject.execute(query)
		lruCountTuple = myCursorObject.fetchall()
		lruCount = lruCountTuple[0]
		print('The least count is  :'+str(lruCount[0]))
		
		###Taking the lruCount[0] which is a string extracted from the lruCountTuple for fetching all the records with minimum count
		query = "SELECT * FROM CACHEVIDEOSDBTABLE WHERE COUNT = '%s' "%(lruCount[0])
		rsNumberOfRecords = myCursorObject.execute(query)
		lruRecords = myCursorObject.fetchall()
		
		###Displaying the video file names which are least recently used. There is a possibility that multiple records can be the resultset
		print('The video files which are least used are ....')
		for record in lruRecords:
			print(record[1])
			time.sleep(1)
		
		#Checking the resultset of number of records with least recently used count. if resultset is one then only one record is there which is LRU
		#Delete the record with least count from cache table
		if rsNumberOfRecords == 1:
			#Deleting the least recently used record from the CacheDBTable
			print('Deleting the Least Recently Used Record...with minimum count')
			query = "DELETE FROM CACHEVIDEOSDBTABLE WHERE COUNT='%s' "%(lruCount[0])
			myCursorObject.execute(query)
			myDBConnectObject.commit()

		#Checking for multiple records with least count and based on timestamp retrieving the oldest timestamp record
		else:
			#Deleting the least recently used record from the CacheDBTable
			print('Found more than one record which has minimum count...')
			print('Deleting the Least Recently Used Record ... with minimum count and oldest timestamp...')
			#creating a view to select all the LRU Count records
			createViewQuery = "CREATE OR REPLACE VIEW LRURecords AS SELECT * FROM  cachevideosdbtable WHERE COUNT = (SELECT MIN(COUNT) FROM cachevideosdbtable)"
			myCursorObject.execute(createViewQuery)
			#Selecting the oldest timestamp record from the view of LRU Count Records
			selectTheOldestTimestampQuery = "SELECT VIDEO_ID FROM cachevideosdbtable WHERE Accessed_Timestamp = (SELECT MIN(Accessed_Timestamp) FROM lrurecords)"
			myCursorObject.execute(selectTheOldestTimestampQuery)
			videoIDTobeDeletedTuple = myCursorObject.fetchall()
			print(str(videoIDTobeDeletedTuple))
			videoIDTobeDeleted = videoIDTobeDeletedTuple[0]
			print('The video ID to be deleted from cache using LRU scheme is:  '+str(videoIDTobeDeleted[0]))
			query = "DELETE FROM CACHEVIDEOSDBTABLE WHERE VIDEO_ID='%s' "%(videoIDTobeDeleted[0])
			myCursorObject.execute(query)
			myDBConnectObject.commit()
			
		##Cache Replacement implementation
		print('Cache Replacement in progress....')
		
		#fetching the video data from the AllVideos database table
		#this video is not available in the cache, so we have to replace a record in the case with this record(only one record of cache miss will be the resultset)
		query = "SELECT * FROM ALLVIDEOSDBTABLE where VIDEO_NAME ='%s' "%(randomFile)
		myCursorObject.execute(query)
		InsertRecordTuple= myCursorObject.fetchall()
		InsertRecord = InsertRecordTuple[0]
		#displaying the cache miss video file data
		print('The record that will be replaced in the CacheDBTable is')
		print(InsertRecordTuple)
		selectQuery = "SELECT * FROM ALLVIDEOSDBTABLE WHERE VIDEO_NAME = '%s' "%(randomFile)
		myCursorObject.execute(selectQuery)
		myResultSet = myCursorObject.fetchone()
		videoID = myResultSet[0]
		videoName = myResultSet[1]
		videoLocation = myResultSet[2]
		videoViewCount = 1
		videoAccessedTimeStamp = 'NULL'
		insertQuery = "INSERT INTO CACHEVIDEOSDBTABLE (VIDEO_ID,VIDEO_NAME,VIDEO_LOCATION,COUNT,ACCESSED_TIMESTAMP) VALUES ('%s','%s','%s','%s','%s')"%(videoID,videoName,videoLocation,videoViewCount,videoAccessedTimeStamp)
		myCursorObject.execute(insertQuery)
		updateQuery = "UPDATE CACHEVIDEOSDBTABLE SET ACCESSED_TIMESTAMP = CURRENT_TIMESTAMP() WHERE VIDEO_NAME = '%s' "%(randomFile)
		myCursorObject.execute(updateQuery)
		myDBConnectObject.commit()
		