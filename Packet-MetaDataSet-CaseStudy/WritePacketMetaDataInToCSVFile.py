import os
import csv
import random
import datetime
import time

def Get_MACID():
	macid = random.randint(111111111111111,999999999999999)
	mac_hex = hex(macid).replace('0x', '').upper()
	Formatted_MACID = '-'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
	return Formatted_MACID
	
def Get_Time():
	mySystemTime = datetime.datetime.now()
	time = mySystemTime.strftime(myTimeFormat)
	return time


delimiter = ','
myCSVFileName = input('Enter a CSV Filename :')
myTimeFormat = '%d-%B-%y %H:%M:%S'

fileExists = os.path.isfile(myCSVFileName)

with open(myCSVFileName,'a',newline='') as appendInToCSVFile:
	csvHeader = ['SENDER','PACKET_ID','RECEIVER','ORIGINATION_TIME','RECEPTION_TIME','LIFETIME','DELTA','DECISION']
	MyHeader = csv.DictWriter(appendInToCSVFile,fieldnames=csvHeader)
	if not fileExists:
            MyHeader.writeheader()
	ID = 1
	while(ID <= 2):
		randomMacID = Get_MACID()
		sender = "User_"+randomMacID
		randomMacID = Get_MACID()
		receiver = "User_"+randomMacID
		packetID = 'Packet'+str(1000+ID)
		pktOrgTime = Get_Time()
		time.sleep(random.randint(1,3))
		pktRecvTime = Get_Time()
		timeDelta = datetime.datetime.strptime(pktRecvTime,myTimeFormat) - datetime.datetime.strptime(pktOrgTime,myTimeFormat)
		totalSeconds=timeDelta.total_seconds()
		lifetime = random.randint(1,10)
		if(lifetime >= totalSeconds):
			decision = 'Accept'
		else:
			decision = 'Reject'
		appendInToCSVFile.write(sender)
		appendInToCSVFile.write(delimiter)
		appendInToCSVFile.write(packetID)
		appendInToCSVFile.write(delimiter)
		appendInToCSVFile.write(receiver)
		appendInToCSVFile.write(delimiter)
		appendInToCSVFile.write(pktOrgTime)
		appendInToCSVFile.write(delimiter)
		appendInToCSVFile.write(pktRecvTime)
		appendInToCSVFile.write(delimiter)
		appendInToCSVFile.write(str(lifetime))
		appendInToCSVFile.write(delimiter)
		appendInToCSVFile.write(str(totalSeconds))
		appendInToCSVFile.write(delimiter)
		appendInToCSVFile.write(decision)
		appendInToCSVFile.write('\n')
		ID = ID + 1

	

