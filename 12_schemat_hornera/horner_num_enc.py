def horner( n, m ):
	r = n.pop( 0 )

	while len( n ) > 0:
		r = r*m + n.pop( 0 )

	return r


if __name__ == '__main__':
	
	num = '4223213'
	system = 5			#system piątkowy

	l_num = list( map( int, list( num )))

	# wyjaśnienie powyższej liniii

	# list( num )							['4', '2', '2', '3', '2', '1', '3']	 		rozdziela string na listę ZNAKÓW
	# map( int, list( num ) )				<map object at 0x7f69a79d0580>				zamienia listę znaków na map object
	# list( map( int, list( num ) ) )		[4, 2, 2, 3, 2, 1, 3]						zamienia map object z powrotem na listę ale tym razem INT-ÓW (liczb całkowitych)

	print("Liczba 4223213 w systemie 5-tkowym to", horner( l_num, 5), "w systemie dziesiętnym")		#70433