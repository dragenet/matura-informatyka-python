def reszta( n ):

	#Funkcja realizująca wydawanie resztę metodą zachłanną
	#Parameters:
	#	 n (int): Warość reszty
	#
	#Returns:
	#	(int): Ilość banknotów i monet do wydania

	denomins = [1, 2, 5, 10, 20, 50, 100, 200, 500]		#nominały

	change = []
	
	for d in denomins[::-1]:	#iterates denomins in reverse
		while n >= d:
			n -= d
			change.append(d)

	return len( change )


if __name__ == '__main__':

	l = int( input( "Podaj liczbę: " ) )
	res = reszta( l )

	print( "Potrzebna ilość banknotów i monet by wydać resztę: ", res )