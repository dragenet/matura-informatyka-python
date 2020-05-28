def horner( n, m ):
	r = n.pop( 0 )

	while len( n ) > 0:
		r = r*m + n.pop( 0 )

	return r


if __name__ == '__main__':
	print( horner([1,-4,7,-6], 2) )