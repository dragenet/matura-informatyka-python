def fiborek( n, a = 0, b = 1 ):

	#Funkcja iteracyjna zwracająca n-wyrazów ciągu fibonaciego
	#Parameters:
	#	 n (int): Liczba wyrazów ciągu fibbonaciego 
	#	 a (int): Pierwszy wyraz ciągu fibbonaciego, nie używać
	#	 b (int): Drugi wyraz ciągu fibbonaciego, nie używać
	#
	#Returns:
	#	fib (int): Wartość n-tego wyrazu ciągu fibbonaciego

	if n == 1:
		return a

	c = a+b

	return fiborek(n-1, b, c)
		
	

if __name__ == "__main__":
	l = int( input( "Podaj liczbę wyrazów ciągu fibbonaciego: ") )
	res = fiborek(l)

	print(l, "wyraz ciągu fibbonaciego ma wartość", res)