from czydoskonala import czyDoskonala 

testdata = list( map( int ,open( "doskonale.txt" ).read().split("\n") ) )

print(testdata)


def test(data, testfunc, verbose=False):

	j = 0

	if verbose:
		print("Number","		","Response")

	for i in range(1, data[-1]+1):

		res = testfunc(i)

		if verbose:
			print(i,"		",res)

		if i == data[j] and res == True:
			j+=1

		elif i == data[j] and res == False:
			return False

		elif i != data[j] and res == True:
			return False

	return True

print( "Running test..." )
result = test(testdata, czyDoskonala, True)

if result:
	print( "Test: success" )
else:
	print( "Test: Failed")