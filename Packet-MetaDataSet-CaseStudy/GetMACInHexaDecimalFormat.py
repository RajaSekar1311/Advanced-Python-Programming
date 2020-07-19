'''
#Universally Unique Identifiers UUID Module
import uuid
myMACID = uuid.getnode()
print(myMACID)
print(hex(myMACID))
print(hex(myMACID).replace('0x',''))
print(hex(myMACID).replace('0x', '').upper())
mac_hex = hex(myMACID).replace('0x', '').upper()
Formatted_MACID = '-'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
print(Formatted_MACID)
'''
import uuid
import random

def Get_MACID():
	macid = random.randint(111111111111111,999999999999999)
	#macid = 123658568936176 #Real MACID
	mac_hex = hex(macid).replace('0x', '').upper()
	Formatted_MACID = '-'.join(mac_hex[i: i + 2] for i in range(0, 11, 2))
	return Formatted_MACID

Formatted_MACID = Get_MACID()
print(Formatted_MACID)

'''
Physical Address
==================
3C-A8-2A-AD-80-47
70-77-81-13-2A-F0    707781132af0
70-77-81-13-2A-EF

123658568936176
0x707781132af0
707781132af0


70-77-81-13-2A-F0
'''
