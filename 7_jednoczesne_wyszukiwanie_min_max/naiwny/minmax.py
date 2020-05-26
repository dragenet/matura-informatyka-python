def minmax( n ):
	#Funkcja wyszukuje min i max w liście algorytmem optymalnym
	#Parameters:
	#	 n (list): Lista wartości
	#
	#Returns:
	#	minimum,maximum (tuple): Warości min i max

	MIN = MAX = n[ 0 ]

	for i in n[1:]:		#pomijamy pierwszy element w n
		if i > MAX:
			MAX = i

		if i < MIN:
			MIN = i

	return ( MIN, MAX )


if __name__ == '__main__':

	l = [ 10, 0, 5, 3, 20, 1, 54] 

	res = minmax( l )

	print( "Wartość minimalna:", res[0] )
	print( "Wartość maksymalna:", res[1] )