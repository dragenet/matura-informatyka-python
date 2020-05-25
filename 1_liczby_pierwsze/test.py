from czypierwsza import czyPierwsza 

testdata = list( map( int ,open( "pierwsze1000.txt" ).read().split() ) )


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

result = test(testdata, czyPierwsza, True)

if result:
	print( "Test: success" )
else:
	print( "Test: Failed")