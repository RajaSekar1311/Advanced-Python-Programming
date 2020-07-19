import names
import random
regNum = 1001
while(regNum <=1003):
	firstName = names.get_first_name()
	lastName = names.get_last_name()
	studentName = firstName+' '+lastName
	studentGender = random.choice(['Male','Female'])
	studentDepartment = random.choice(['CSE','ECE','EEE','Mechanical','Civil','EIE'])
	emailTag = random.choice(['@gmail.com','@yahoo.co.in','@rediffmail.com','@hotmail.com'])
	studentEmail = firstName+lastName+emailTag
	studentContact = random.randint(9986000000,9986999999)
	print(regNum,studentName,studentGender,studentDepartment,studentEmail,studentContact)
	regNum = regNum+1

'''
import names
import random
regNum = 1001
while(regNum <=1003):
	#studentName = names.get_full_name()
	firstName = names.get_first_name()
	lastName = names.get_last_name()
	studentName = firstName+' '+lastName
	studentGender = random.choice(['Male','Female'])
	studentDepartment = random.choice(['CSE','ECE','EEE','Mechanical','Civil','EIE'])
	emailTag = random.choice(['@gmail.com','@yahoo.co.in','@rediffmail.com','@hotmail.com'])
	#studentEmail = studentName+emailTag
	studentEmail = firstName+lastName+emailTag
	studentContact = random.randint(9986000000,9986999999)
	print(regNum,studentName,studentGender,studentDepartment,studentEmail,studentContact)
	regNum = regNum+1
'''
'''
import random
regNum = 1001
while(regNum <=1003):
	studentName = 'Student'+str(regNum)
	studentGender = random.choice(['Male','Female'])
	studentDepartment = random.choice(['CSE','ECE','EEE','Mechanical','Civil','EIE'])
	emailTag = random.choice(['@gmail.com','@yahoo.co.in','@rediffmail.com','@hotmail.com'])
	studentEmail = studentName+emailTag
	studentContact = random.randint(9986000000,9986999999)
	print(regNum,studentName,studentGender,studentDepartment,studentEmail,studentContact)
	regNum = regNum+1
'''