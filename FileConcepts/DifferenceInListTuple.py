#To understand the concept of mutable List and immutable Tuple

myList = [1,2,3,4.567,'Python']
myTuple = (1,2,3,4.567,'Python')
print(myList)
print(type(myList))
print(myTuple)
print(type(myTuple))
del(myList[2])
print(myList)
del(myTuple[2])
print(myTuple)