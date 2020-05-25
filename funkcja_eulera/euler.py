def euklidrek( a, b ):
	if b == 0:
		return a

	c = a%b

	return euklidrek( b, c )

def tocjent(n):
	c = 0

	for i in range(1, n+1):
		if(euklidrek(n, i) == 1):
			c+=1
	return c

l = int( input("Podaj liczbę: ") )
print(tocjent(l))