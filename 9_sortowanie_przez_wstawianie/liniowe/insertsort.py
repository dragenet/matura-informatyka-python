def insertsort( n ):

	#Funkcja sortuje zbiór n algorymem sortowania przez wstawianie
	#Parameters:
	#	 n (list): Zbiór nieposortowany
	#
	#Returns:
	#	 s (list): Zbiór posortowany


	s = []

	s.append( n.pop(0) )

	while len( n ) > 0:
		e = n.pop(0)
		for i in range( len( s ) ):
			if e <= s[ i ]:
				s.insert( i, e )
				break

			if i == ( len(s) - 1 ):
				s.append( e )
				break



	return s

if __name__ == '__main__':
	
	l = [ 10, 30, 5, 3, 20, 1, 54] 

	print( insertsort( l ) )

