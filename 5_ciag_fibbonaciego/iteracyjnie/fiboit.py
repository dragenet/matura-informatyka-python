def fiboit( n ):

	#Funkcja iteracyjna zwracająca n-wyrazów ciągu fibonaciego
	#Parameters:
	#	 n (int): Liczba wyrazów ciągu fibbonaciego 
	#
	#Returns:
	#	fib (int): Wartość n-tego wyrazu ciągu fibbonaciego
		
	fib = [0, 1]
	if n < 3:
		return fib[n-1]

	for i in range( 2, n ):
		x = fib[i-1] + fib[i-2]
		fib.append(x)

	return fib[-1]


if __name__ == "__main__":
	l = int( input( "Podaj liczbę wyrazów ciągu fibbonaciego: ") )
	res = fiboit(l)

	print(l, "wyraz ciągu fibbonaciego ma wartość", res)
