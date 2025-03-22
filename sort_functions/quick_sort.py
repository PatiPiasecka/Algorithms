"""
QUICK SORT 
dzieli tablicę na mniejsze części, sortuje je rekurencyjnie, a następnie łączy wyniki.

Kluczowym jest wybranie tzw. pivota
Pivot to element względem którego porządkujemy tablice

Złożoność obliczeniowa: - wybor Lomuto i Hoare nie ma wiekszego znaczenia
O(n^2) - najgorszy (np. gdy tablica jest posortowana a pivotem jest skrajny element)
O(n log n) - średni (gdy pivotem np. jest mediana)
"""
"""
JAK DZIAŁA PARTITION?
funkcja partition partycjonuje naszą tablice - dzieli wzgledem pivota

WERSJA LOMUTO:
Pivotem jest ostatni element
dzieli tablice na dwie czesci wzgledem pivota
Celem jest podział tablicy na trzy sekcje:

1) Elementy mniejsze (lub równe) od pivota,
2) Pivot
3) Elementy większe od pivota.

Przed partycjonowaniem: [3, 6, 8, 2, 1, 5]
Po partycjonowaniu:     [3, 2, 1, 5, 6, 8]
                        <───┬───>   <───>
                        ≤ pivot    > pivot

INPUT:
A - tablica liczb
p - indeks poczatkowy aktualnie sortowanej tablicy (to bedzie sie zmieniac)
r - indeks koncowy ...

WERSJA HOARE:
Pivotem jest zazwyczaj pierwszy element tablicy 
(można też wybrać środkowy lub losowy).

i - zaczyna od lewej strony (i = low), 
szuka elementów ≥ pivot,

j - zaczyna od prawej strony (j = high), 
szuka elementów ≤ pivot.

Przed partycjonowaniem: [5, 3, 8, 4, 2, 7, 1, 6]
Po partycjonowaniu:     [5, 3, 1, 4, 2, 7, 8, 6]
                          <──────┬─────>   <───>
                           ≤ 5       > 5

INPUT:
A - tablica liczb
p - indeks poczatkowy aktualnie sortowanej tablicy (to bedzie sie zmieniac)
r - indeks koncowy ...

3. Różnice między Hoare a Lomuto
Cecha	                                Hoare	                        Lomuto
Wybór pivota	               Pierwszy/środkowy element	        Ostatni element
Liczba zamian	               Mniejsza (efektywniejsza)	            Większa
Pozycja pivota	             Nie musi być na swoim miejscu	      Jest na swoim miejscu
Wydajność dla duplikatów	        Lepsza	                            Gorsza

"""
def lomuto_partition(A, p, r):
    pivot = A[r] #pivotem bedzie ostatni element
    i = p-1

    for j in range (p, r):
        if A[j]<=pivot:
            i+=1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[r] = A[r], A[i + 1]
    return i+1 #zwroc pozycje pivota

def hoare_partition (A, p, r):
    pivot = A[p] #pivotem jest pierwszy element
    i = p-1
    j = r+1

    while True:
        i += 1
        while A[i] < pivot: #szukaj elementow >= pivot
            i += 1
        j -= 1
        while A[j] > pivot: #szukaj elementow <= pivot
            j -= 1
        if i >= j: #do tego momentu elementy beda sie swapowac
            return j #zwroc granice partycjonowania
        A[i], A[j] = A[j], A[i]

"""
JAK DZIAŁA QUICK SORT?
- funkcja wywoluje partition, rekurencyjnie zaweza zakres
Tym samym sortując tablice 

INPUT:
A - tablica liczb
p - ....
r - ....

Ponizej wersja z hoare (mozna podmienic)
"""

def quick_sort(A, p, r):
    if p<r:
        q = hoare_partition(A, p, r)
        quick_sort(A, p, q) #sortuj lewą czesc (dla lomuto q-1)
        quick_sort(A, q+1, r) #sortuj prawa czesc
