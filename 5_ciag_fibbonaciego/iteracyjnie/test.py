from fiboit import fiboit 

testdata = list( map( int ,open( "513fibotest.txt" ).read().split("\n") ) )

#print(testdata)


def test(data, testfunc, verbose=False):

	

	if verbose:
		print("Number (n) ","		","Result")

	for i in range(1, len(data)+1 ):

		res = testfunc(i)

		if res == data[i-1] :
			if verbose:
				print(i,"			","Success")

		else:
			if verbose:
				print( i, "			 ", "Failed", "		:	", res, "is not", data[i-1])
			return False

	return True

print( "Running test..." )
result = test(testdata, fiboit, False)	#użyj test(testdata, fiboit, True) for extended output

if result:
	print( "Test: Success" )
else:
	print( "Test: Failed")