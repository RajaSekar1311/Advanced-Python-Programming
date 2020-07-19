import datetime
import random
def selectRandomTimeStamp():
	start = datetime.datetime.now()
	print('The Current Date and Time is : ',start)
	timeDifference = datetime.timedelta(numberOfDays)
	print('The Time difference is : ',timeDifference)
	end = start + timeDifference
	print ('The End Date and Time is : ',end)
	PastDay = (end - start) * random.random()
	print (PastDay)
	randomTimeStamp = start + PastDay
	print ('The final selected Date and Time is : ',randomTimeStamp)
numberOfDays = 60
selectRandomTimeStamp()