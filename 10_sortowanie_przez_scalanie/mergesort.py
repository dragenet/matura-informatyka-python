def merge( a, b ):
	#i, j = 0
	c = []

	while len( a ) != 0 or len( b ) != 0:
		if len ( a ) == 0:
			c.extend( b )
			break

		if len( b ) == 0:
			c.extend( a )
			break

		if a[0] <= b[0]:
			x = a.pop( 0 )
			c.append( x )

		else:
			x = b.pop( 0 )
			c.append( x )


	return c

def mergesort( n ):

	#Funkcja sortuje zbiór n algorytmem sortowania przez scalanie
	#Parameters:
	#	 n (list): Zbiór nieposortowany
	#
	#Returns:
	#	 (list): Zbiór posortowany
	
	if len( n ) > 1:
		d = int( len( n ) / 2 )

		a = mergesort( n[:d] )
		b = mergesort( n[d:] )

		return merge( a, b )

	else:
		return n



if __name__ == '__main__':
	
	l = [ 10, 30, 5, 3, 20, 1, 54] 

	print( mergesort( l ) )