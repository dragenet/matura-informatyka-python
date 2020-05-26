from math import sqrt

def rozkl(n):
	c = []

	k = 2

	while( n > 1):
		while( n%k == 0 ):
			c.append(k)
			n/=k
		k+=1

	return c

if __name__ == '__main__':
	
	l = int( input("Podaj liczbę: "))
	print( "Czynniki to: " )

	for i in rozkl(l):
		print(i, "	")