'''
a,b,c,d = 10, int(10), int('10'),int('1010',2)
print("The value of a is:",a)
print("The id of a is:",id(a))
print("The value of b is:",b)
print("The id of b is:",id(b))
print("The value of c is:",c) 
print("The id of c is:",id(c))
print("The value of d is:",d)
print("The id of d is:",id(d))
'''
'''
#Understand zip
tupleA = ("Naga", "Kishore", "Shradha")
tupleB = ("Raju", "Kumar", "Kishan")
zippedTupleC = zip(tupleA, tupleB)
print(type(zippedTupleC))
print(zippedTupleC)
print('Tuple A is:   ',tupleA)
print('Tuple B is:   ',tupleB)
print('The Tuple C after invoking zip method is:   ',list(zippedTupleC))
'''
resultBooleanValue = (all([i is j for i, j in list(zip(range(-5, 257, 1), range(-5, 257, 1)))]))
print(resultBooleanValue)

resultBooleanValue = (any([i is j for i, j in list(zip(range(257, 1000, 1), range(257, 1000, 1)))]))
print(resultBooleanValue)

resultBooleanValue = (all([i is j for i, j in list(zip(range(-6, 1000, 1), range(-6, 1000, 1)))]))
print(resultBooleanValue)


