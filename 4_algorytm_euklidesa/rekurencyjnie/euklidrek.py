def euklidrek( a, b ):
	print(a, "		", b)
	if b == 0:
		return a

	c = a%b

	return euklidrek( b, c )


l = int( input("Podaj pierwszą liczbę: ") )
m = int( input("Podaj drugą liczbę: ") )

d = euklidrek( l, m )

print( "Ich NWD to: ", d )