def euklidit( a, b ):
	while b != 0:
		c = a%b
		a = b
		b = c
	return a


l = int( input("Podaj pierwszą liczbę: ") )
m = int( input("Podaj drugą liczbę: ") )

d = euklidit( l, m )

print( "Ich NWD to: ", d )