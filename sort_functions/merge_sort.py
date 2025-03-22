"""
MERGE SORT - OPIS ALGORYTMU
Jego działanie polega na rekurencyjnym dzieleniu tablicy na mniejsze części, sortowaniu ich, 
a następnie scalaniu (ang. merge) w uporządkowaną całość.

1. Dzielenie (Divide)
Tablica jest rekurencyjnie dzielona na dwie równe (lub prawie równe) części, 
aż do momentu, gdy każda część składa się z jednego elementu. 
Jednoelementowa tablica jest z założenia już posortowana.

2. Scalanie (Merge)
Posortowane podtablice są łączone (scalane) w większą, uporządkowaną tablicę. 
Proces scalania polega na porównywaniu elementów z obu podtablic i umieszczaniu 
ich w odpowiedniej kolejności w nowej tablicy.

ZŁOŻONOŚĆ CZASOWA -- O(n logn)
"""
def merge_sort_for_the_tabs(tab):
    if len(tab)>1: #warunek brzegowy
        mid = len(tab)//2
        left = tab[:mid]
        right = tab[mid:]
        
        merge_sort_for_the_tabs(left)
        merge_sort_for_the_tabs(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                tab[k]=left[i]
                i+=1
            else:
                tab[k]=right[j]
                j+=1
            k+=1
        
        while j<len(right):
            tab[k]=right[j]
            k+=1
            j+=1
        while i<len(left):
            tab[k]=left[i]
            k+=1
            i+=1   
    return tab

#merge sort for the linked list

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def find_mid_in_the_linked_list(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right): #merge two sorted linked list
    if not left:
        return right
    if not right:
        return left
    
    if left.val<right.val:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(right.next, left)
    
    return result 

def merge_sort(head):
    if not head or not head.next: #if linked list is empty or has only 1 element
        return head
    mid = find_mid_in_the_linked_list(head)
    mid_next = mid.next
    mid.next = None #divide in two linked list
    left = merge_sort(head)
    right = merge_sort(mid_next)
    
    return merge(left, right)
