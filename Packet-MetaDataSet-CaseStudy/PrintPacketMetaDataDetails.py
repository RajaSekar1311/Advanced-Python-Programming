import os
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


myTimeFormat = '%d-%B-%y %H:%M:%S'
ID = 1
while(ID <= 3):
	randomMacID = Get_MACID()
	sender = "User_"+randomMacID
	randomMacID = Get_MACID()
	receiver = "User_"+randomMacID
	packetID = 'Packet'+str(1000+ID)
	pktOrgTime = Get_Time()
	time.sleep(random.randint(1,10))
	pktRecvTime = Get_Time()
	timeDelta = datetime.datetime.strptime(pktRecvTime,myTimeFormat) - datetime.datetime.strptime(pktOrgTime,myTimeFormat)
	totalSeconds=timeDelta.total_seconds()
	lifetime = random.randint(1,5)
	print('Sender:   ',sender)
	print('Packet ID:   ',packetID)
	print('Receiver:   ',receiver)
	print('Packet Org Time:  ',pktOrgTime)
	print('Packet Recv Time:  ',pktRecvTime)
	print('Packet Lifetime is:	',lifetime)
	print('Delay is:		'+str(totalSeconds)+'  seconds')
	if(lifetime >= totalSeconds):
		print('Packet Accept')
	else:
		print('Packet Reject')
	ID = ID + 1