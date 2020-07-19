import platform
cacheBegin, cacheEnd = 0, 0
print(cacheBegin)
print(cacheEnd)
for i in range( -500, 0): 
	if i is int(str(i)):
		cacheBegin = i
		break

for i in range( cacheBegin, 500 ):
	if i is not int(str(i)):
		cacheEnd = i - 1
		break

print( "Python version: {} implementation: {}".format( platform.python_version(), platform.python_implementation() ) )
print( "This implementation caches integers {} to {}".format( cacheBegin, cacheEnd ) )
