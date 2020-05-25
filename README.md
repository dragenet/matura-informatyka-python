# Matura z informatyki - Python

W tym repozytorium prezentuję rozwiązania zagadnień programistycznych do matury z informatyki w języku Python.
Zagadnienia wg. wymagań umieszczonych na stronach 110 - 114 książki ["Tom 6 Edukacja matematyczna i techniczna"](http://www.bc.ore.edu.pl/dlibra/docmetadata?id=229)

1. Algorytmy na liczbach całkowitych, np.:
    - reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym,
    - sprawdzanie, czy liczba jest liczbą pierwszą, doskonałą,
    - rozkładanie liczby na czynniki pierwsze,
    - iteracyjna i rekurencyjna realizacja algorytmu Euklidesa,
    - iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego,
    - wydawanie reszty metodą zachłanną,


2. Algorytmy wyszukiwania i porządkowania (sortowania), np.:
	- jednoczesne znajdowanie największego i najmniejszego elementu w zbiorze: algorytm naiwny i optymalny,
	- algorytmy sortowania ciągu liczb: bąbelkowy, przez wybór, przez wstawianie liniowe lub binarne, przez scalanie, szybki, kubełkowy,


3. Algorytmy numeryczne, np.:
 	- obliczanie pierwiastka kwadratowego,
 	- obliczanie wartości wielomianu za pomocą schematu Hornera,
 	- zastosowania schematu Hornera: reprezentacja liczb w różnych systemach liczbowych, szybkie podnoszenie do potęgi,
 	- wyznaczanie miejsc zerowych funkcji metodą połowienia,
 	- obliczanie pola obszarów zamkniętych,


4. Algorytmy na tekstach, np.:
	- sprawdzanie, czy dany ciąg znaków tworzy palindrom, anagram,
	- porządkowanie alfabetyczne,
	- wyszukiwanie wzorca w tekście,
	- obliczanie wartości wyrażenia podanego w postaci odwrotnej notacji polskiej,


5. Algorytmy kompresji i szyfrowania, np.:
	- kody znaków o zmiennej długości, np. alfabet Morse’a, kod Huffmana,
	- szyfr Cezara,
	- szyfr przestawieniowy,
	- szyfr z kluczem jawnym (RSA),
	- wykorzystanie algorytmów szyfrowania, np. w podpisie elektronicznym,
	- algorytmy badające własności geometryczne, np.:
	- sprawdzanie warunku trójkąta,
	- badanie położenia punktów względem prostej,
	- badanie przynależności punktu do odcinka,
	- przecinanie się odcinków,
	- przynależność punktu do obszaru,
	- konstrukcje rekurencyjne: drzewo binarne, dywan Sierpińskiego, płatek Kocha

## Wykaz plików

| Nazwa folderu                                         | Zagadnienie                                                                           |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------|
| *1_liczby_pierwsze/czypierwsza.py*                    | Sprawdzanie czy liczba jest liczbą pierwszą                                           |
| *2_liczby_doskonale/czydoskonala.py*                  | Sprawdzanie czy liczba jest liczbą doskonałą                                          |
| *3_roklad_na_czynniki/rozkl.py*                       | Rozkład liczby na czynniki pierwsze                                          			|
| *4_algorytm_euklidesa/iteracyjnie/euklidit.py*        | Algorytm euklidesa iteracyjnie                                                        |
| *4_algorytm_euklidesa/rekurencyjnie/euklidrek.py*     | Algorytm euklidesa rekurencyjnie                                                      |
| *5_ciag_fibbonaciego/iteracyjnie/fiboit.py*			| Ciąg fibbonaciego iteracyjnie															|
| *5_ciag_fibbonaciego/rekurencyjnie/fiborek.py*		| Ciąg fibbonaciego iteracyjnie															|
| *6_wydawanie_reszty/reszta.py*						| Wydawanie reszty metodą zachłanną														|
| *funkcja_eulera/euler.py*								| Dodatek: Implementacja funcji eulera, element algorytmu RSA							|

Jeśli w jakimś folderze znajdziesz plik *test.py* to jest to plik automatycznie testujący algorytm korzystając ze zbioru testowego w pliku .txt

W miarę rozwiązania kolejnych zagadnień będę aktualizował to repozytorium
