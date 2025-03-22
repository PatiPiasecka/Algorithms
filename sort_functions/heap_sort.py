#heap sort 

"""
MAX HEAP - sortowanie rosnące (największy element ma indeks 0) - drzewo binarne, 
gdzie wartość każdego rodzica jest większa lub równa wartościom jego dzieci.

1) Przekształć tablicę w kopiec maksymalny, tak aby największy element znalazł się w korzeniu (indeks 0)

2) Ekstrakcja maksymalnego elementu - zamień korzeń (największy element) z ostatnim elementem kopca, 
a następnie zmniejsz rozmiar kopca o 1.

3) Przywrócenie własności kopca - przywróć własność kopca dla nowego korzenia, używając procedury heapify.

4) Powtarzaj kroki 2–3 - kontynuuj, aż cała tablica zostanie posortowana.
"""

"""
CO ROBI HEAPIFY?
upewnia się, że wartość rodzica jest większa lub równa wartościom jego dzieci

UWAGA! 
Heapify nie układa całego kopca poprawnie (przynajmniej nie taki jest jej cel) 
- heapify jedynie zapewnia, że dzieci są mniejsze od rodzica

INPUT:
A - tablica liczb
n - aktualny rozmiar kopca
i - indeks korzenia

O(log n)
"""

def heapify (A, n, i):
    max_ind = i
    left = 2*i + 1 #indeks dziecka po lewej stronie
    right = 2*i + 2 #indeks dziecka po prawej stronie

    #sprawdzam czy lewe dziecko jest mniejsze od korzenia
    if left < n and A[left] > A[max_ind]:
        max_ind = left
    #analogicznie prawe dziecko
    if right < n and A[right] > A[max_ind]:
        max_ind = right
    
    #jesli najwiekszy nie jest korzeniem, swapuj
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind) #rekurencja dla nowego korzenia

"""
CO ROBI BUILD_HEAP?
- funkcja ma za zadanie z tablicy zrobić kopiec maksymalny 
- funkcja wykorzystuje wczesniejsza funkcje heapify aby zachować strukture kopca
- NIE SORTUJE TABLICY - zapewnia strukture kopca maksymalnego ale jej nie sortuje 

INPUT:
A - tablica liczb

O(n)
"""

def build_heap(A):
    n = len(A)
    parent = n//2-1 #ostatni rodzic

    #od parent poniewaz nie sprawdzam liści - one nie mają potomstwa
    for i in range (parent, -1, -1):
        heapify(A, n, i)

"""
CO ROBI HEAP SORT?
- sortuje nasz kopiec

Sortowanie odbywa sie w nastepujacy sposob:
po znalezieniu najwiekszego elementu trafia on na koniec kopca (ostatni indeks) i traktowany jest jako czesc posortowana,
zatem każde kolejne wywołanie funkcji odbywa się rekurencyjnie (wykluczajac ten element) - funkcja zakonczy się gdy kopiec będzie
miał 1 element - czyli i będzie równe 0 
"""
def heap_sort(A):
    n = len(A)
    build_heap(A) #zbudujmy kopiec dla obecnych elementow w tablicy

    #dlaczego petla jest od konca? - na samym poczatku bierzemy wszystkie elementy a potem po znalezieniu najwiekszego 
    # - zmniejszamy ich ilosc - zamysl podobny troche do bubble_sort gdzie najwiekszy element przestaje byc brany pod uwage
    for i in range (n-1, 0, -1):
        A[0], A[i] = A[i], A[0] #wrzucam korzen na koniec 
        heapify(A, i, 0) #nie mam gwarancji ze korzen byl max dla tablicy wiec naprawiajac kopiec - uzyskam ta pewnosc


"""
ZALETY HEAP_SORT

złożoność czasowa - O(n log n)
złożoność pamięciowa - O(1) - PRZEWAGA NAD MERGE_SORTEM
"""