"""
ALGORYTMY LINIOWE SORTOWANIA

Poniższe algorytmy mają specyficzne warunki sortowania aby rzeczywiście osiągnąć O(n)

Dla dowolnych tablic bez żadnych warunków początkowych najlepszym sortowaniem będzie sortowanie o złożoności
obliczeniowej O(n log n) 
"""

#counting_sort
"""
Potrzebujemy znać zakres liczb występujących w tablicy np. [0, 100] oraz max element - musi byc niewielki (k-1).
Wtedy osiągniemy O(n+k), dla ponizszego algorytmu uwzgledniamy liczby naturalne z malego zakresu
- BRAK UŁAMKÓW
- BRAK LICZB UJEMNYYCH

Algorytm polega na utworzeniu pustej tablicy (B) o k pozycjach. Zliczamy elementy wystepujace w tablicy A za pomoca
utworzonej tablicy B i nastepnie wykorzystujac sumy skumulowane (ilosc elementow <= elem)
odtwarzam posortowaną już tablice A (przy pomocy tablicy wynikowej C)

INPUT:
A - tablica liczb
k - liczba o 1 większa od maxa występującego w tablicy
"""

def counting_sort(A, k):
    n = len(A)
    B = [0]*k

    for elem in A: #zliczanie
        B[elem] += 1
    
    for i in range (1, k): #sumy skumulowane B[i] = j gdzie j jest rowne ilosci elem <= i w tablicy A
        B[i] += B[i-1]
    
    C = [0]*n #tablica wynikowa
    for i in range (n-1, -1, -1):
        B[A[i]] -= 1 
        C[B[A[i]]] = A[i] 
    for i in range (n):
        A[i] = C[i]
    return A

#bucket_sort
"""
Sortujemy liczby wymierne z zakresu [min_val,max_val] (dla naszego przykladu [0,1]) 
- wygenerowane zgodnie z rozkladem jednostajnym

Krok 1:
dzielimy przedział [min_val, max_val] na n przedziałow po 1/n każdy
np: n = 10
Bucket 0: [0.0, 0.1)
Bucket 1: [0.1, 0.2)
Bucket 2: [0.2, 0.3)
Bucket 3: [0.3, 0.4)
Bucket 4: [0.4, 0.5)
Bucket 5: [0.5, 0.6)
Bucket 6: [0.6, 0.7)
Bucket 7: [0.7, 0.8)
Bucket 8: [0.8, 0.9)
Bucket 9: [0.9, 1.0)

Krok 2:
Liczby z kazdego przedzialu sortujemy osobno i nastepnie sklejamy przedzialy

Złożoność obliczeniowa:
O(n) - gdy liczby są rownomiernie rozlozone po kubelkach 
O(n^2)  - gdy wszystkie liczby trafią do jednego kubelka

Przewaga algorytmu jest to ze nie sortujemy calej tablicy na raz ale jej czesci a nastepnie laczymy

INPUT:
A - tablica liczb
n - ilosc kubelkow
"""

def bucket_sort (A, n):
    min_val = min(A)
    max_val = max(A)
    range_val = max_val-min_val

    buckets = [[] for _ in range(n)] #tworzenie kubelkow

    #rozmieszczam elementy w kubełkach
    for elem in A:
        if range_val == 0: #wszystkie elementy są rowne i trafiaja do jednego kubelka
            buckets[0].append(elem)
        else:
            index = int(((elem - min_val) / range_val) * n) #szukam do ktorego kubelka powinien trafic - wzor matematyczny
            if index == n: #jesli to max wartosc w tablicy to automatycznie do ostatniego
                index -= 1
            buckets[index].append(elem)
    
    # Krok 2: Sortujemy każdy kubełek i łączymy wyniki
    sorted_A = []
    for bucket in buckets:
        # Sortowanie kubełka (można użyć dowolnego algorytmu, dla uproszczenia uzyjemy wbudowanego sorted)
        sorted_bucket = sorted(bucket)  # Dla O(n log n) w kubełku
        sorted_A.extend(sorted_bucket)
    
    return sorted_A

#radix_sort
"""
Zaczyna sortowac od najmniej znaczacej cyfry (litery) do najbardziej
Musimy znac dlugosc najdluszej liczby - k 

Uzywa algorytmu pomocniczego do sortowania - niech dla nas to bedzie counting_sort przystosowany do cyfr
"""
def counting_sort_radix(A, exp):
    n = len(A)
    C = [0] * n       # Tablica wynikowa 
    B = [0] * 10      # Tablica zliczająca 
    
    # Zliczanie wystąpień cyfr
    for elem in A:
        index = (elem // exp) % 10  # Wyciągamy aktualną cyfrę
        B[index] += 1
    
    # Sumy skumulowane
    for i in range(1, 10):
        B[i] += B[i-1]
    
    # Budowa tablicy wynikowej C
    for i in range(n-1, -1, -1):
        index = (A[i] // exp) % 10
        B[index] -= 1
        C[B[index]] = A[i]
    
    for i in range(n):
        A[i] = C[i]

def radix_sort(A):
    max_val = max(A)
    exp = 1  # Początkowa cyfra (jedności)

    while max_val // exp > 0: #potrzebna nam dlugosc najdluzszego - mozna podac jako argument
        counting_sort_radix(A, exp)
        exp *= 10  # Przejdź do kolejnej cyfry
    return A