import random
from datetime import datetime,timedelta
from time import sleep


class packet():
	def __init__(self,id,routers_Set):
		self.pac_id = id
		self.start_node = random.choice(routers_Set)
		routers_Set.remove(self.start_node)
		self.end_node = random.choice(routers_Set)# starting and ending node cannot be same
		temp = hex(random.randint(111111111111111,999999999999999)).replace('0x','').upper()
		self.sender_mac = '-'.join(temp[i:i+2] for i in range(0,12,2))
		temp = hex(random.randint(111111111111111,999999999999999)).replace('0x','').upper()
		self.reciever_mac = '-'.join(temp[i:i+2] for i in range(0,12,2))
		time = datetime.now()
		self.orig_time = time.strftime("%H:%M:%S")
		routing_time = random.randint(1,30)
		self.prop_time = routing_time
		time = time + timedelta(0,routing_time)
		self.delivery_time = time.strftime("%H:%M:%S")
		self.ttl = random.randint(10,25)
		self.status = None
		if self.prop_time > self.ttl:
			self.status = "Rejected"
		else:
			self.status = "Accepted"
		
	def display(self):
		print("")
		print("Packet ID: ",self.pac_id)
		print("Sender MAC ID: ",self.sender_mac)
		print("Sender Router: ",self.start_node)
		print("Reciever MAC ID: ",self.reciever_mac)
		print("Reciever Router: ",self.end_node)
		print("Origination Time: ",self.orig_time)
		print("Delivery Time: ",self.delivery_time)
		print("Processing Time: ",self.prop_time)
		print("TTL: ",self.ttl)
		print("Packet Status: ",self.status)
	
	def supply(self):
		return ([str(self.start_node),str(self.end_node)])

routers_Set = {'A','B','C','D','E'}
for i in range(1,6):
	new_packet = packet(1000+i)
	new_packet.display()	


