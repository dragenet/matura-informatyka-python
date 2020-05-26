def binsearch( s, el, start, end):

	#Algorytm wyszukiwania binarnego

	if start == end:
		if el < s[ start ]:
			return start
		else:
			return start+1

	center = int( (end -start) / 2 )
	li = start + center
	ri = start + center+1
	if el <= s[ li ]:
		return binsearch(s, el, start, li)
	else:
		return binsearch(s, el, ri, end)


def insertsortbin( n ):

	#Funkcja sortuje zbiór n algorymem sortowania przez wstawianie z użyciem wyszukiwania binarnego
	#Parameters:
	#	 n (list): Zbiór nieposortowany
	#
	#Returns:
	#	 s (list): Zbiór posortowany
	
	s = []

	s.append( n.pop(0) )

	while len( n ) > 0:
		el = n.pop(0)
		i = binsearch( s, el, 0, len(s)-1 )	
		s.insert(i, el)
		#print("\n")

	return s
	



if __name__ == '__main__':
	
	l = [ 10, 30, 5, 3, 20, 1, 54] 

	print( insertsortbin( l ) )

#[x, x, x, x, 4, 5, 6, 7]
