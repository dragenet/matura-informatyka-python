def boublesort( n ):

	#Funkcja sortuje zbiór n algorymem sortowania bąbelkowego
	#Parameters:
	#	 n (list): Zbiór nieposortowany
	#
	#Returns:
	#	 n (list): Zbiór posortowany

	isChanged = True

	while isChanged == True:
		isChanged = False
		for i in range( len( n )-1 ):
			if n[ i ] > n[ i+1 ]:
				x = n[ i+1 ]
				n[ i+1 ] = n[ i ]
				n[ i ] = x
				isChanged = True


	return n


if __name__ == '__main__':
	
	l = [ 10, 0, 5, 3, 20, 1, 54 ] 

	print( boublesort( l ) )