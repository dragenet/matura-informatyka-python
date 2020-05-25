def czyDoskonala(n):
	d = []

	for i in range(1, n-1):
		if n%i == 0:
			d.append(i)

	if sum(d) == n:
		return True
	else:
		return False

if __name__ == "__main__":
	
	l = int(input("Podaj liczbę: "))

	if czyDoskonala(l):
		print("Liczba jest doskonała")

	else:
		print("Liczba nie jest doskonała")