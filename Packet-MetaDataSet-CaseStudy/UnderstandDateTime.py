import datetime
#Default format of Python Date and Time is YYYY-MM-DD HH:MM:SS:Milliseconds
#Myformat is Date-Month-Year Hours:Minutes:Seconds
myTimeFormat = '%d-%B-%Y %H:%M:%S'
MySystemTime = datetime.datetime.now()
print("Default Python Format :",MySystemTime)
#Formatting the default python datetime format to our time format 

MyFormatSystemTime = MySystemTime.strftime(myTimeFormat)

print("Date Time in My format is :",MyFormatSystemTime)

'''
import datetime
#Default format of Python Date and Time is YYYY-MM-DD HH:MM:SS:Milliseconds
CurrentTime = datetime.datetime.now()
print(CurrentTime)

import time
import calendar



ticks = time.time()
print(ticks)

MyTime = time.localtime()
print(MyTime)

Cal = calendar.month(1982,10)
print(Cal)

#timeFormat = '%d-%m-%Y %H:%M:%S'
#timeFormat = '%d/%m/%Y %H.%M'
#timeFormat = '%d-%m-%y %H:%M:%S'
#timeFormat = '%d-%b-%Y %H:%M:%S'
timeFormat = '%d-%B-%Y %H:%M:%S'
MySystemTime = datetime.datetime.now()
print("Default Python Format :",MySystemTime)
MyFormatSystemTime = MySystemTime.strftime(timeFormat)
print("Date Time in My format is :",MyFormatSystemTime)
'''










