import math
def czyPierwsza(n):
	if n < 2:
		return False
	i = 0
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True


if __name__ == '__main__':

	liczba = int(input("Podaj liczbę: "))

	if czyPierwsza(liczba):
		print("Liczba jest pierwsza")
	else:
		print("Liczba nie jest pierwsza")