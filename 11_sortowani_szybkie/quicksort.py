def quicksort( n, start=0, end=None ):

	#Funkcja sortuje zbiór n algorytmem sortowania przez scalanie
	#Parameters:
	#	 n (list): Zbiór nieposortowany
	#	 start (int): Początek zbioru do posortowanie, nie ustawiać
	#	 end (int): Koniec zbioru do posortowania, nie ustawiać
	#
	#Returns:
	#	 n (list): Zbiór posortowany

	if end == None:							# set list end pointer in first run
		end = len( n ) - 1

	p_i =int( ( start + end ) / 2 ) 		#calculate pivot
	p = n[ p_i ]				

	i = start
	j = end

	while i <= j:

		while  n[ i ] < p:
			i+=1

		while n[ j ] > p:
			j-=1
			

		if i <= j:
			n[ i ], n[ j ] = n[ j ], n[ i ]
			i+=1
			j-=1

	if start < j:
		n = quicksort( n, start, j)

	if i < end:
		n = quicksort( n, i, end)

	return n



if __name__ == '__main__':
	
	l = [ 10, 30, 5, 3, 20, 1, 54] 

	print( quicksort( l ) )