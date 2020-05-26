def minlinear( n ):
	m = n[0]

	for i in n:
		if i < m:
			m = i

	return m

def maxlinear( n ):
	m = n[0]

	for i in n:
		if i > m:
			m = i
			
	return m


def minmax( n ):
	#Funkcja wyszukuje min i max w liście algorytmem optymalnym
	#Parameters:
	#	 n (list): Lista wartości
	#
	#Returns:
	#	( MIN, MAX ) (tuple): Warości min i max

	mins = []
	maxs = []

	i=0

	while i+2 <= len( n ):
		if n[i] < n[ i+1 ]:
			mins.append( n[ i ] )
			maxs.append( n[ i+1 ] )

		else:
			mins.append( n[ i+1 ] )
			maxs.append( n[ i ] )
		i+=2

	if len( n )%2 == 1:
		mins.append( n[ i ] )
		maxs.append( n[ i ] )

	MIN = minlinear( mins )
	MAX = maxlinear( maxs )

	return ( MIN, MAX )

if __name__ == '__main__':

	l = [ 10, 0, 5, 3, 20, 1, 54] 

	res = minmax( l )

	print( "Wartość minimalna:", res[0] )
	print( "Wartość maksymalna:", res[1] )