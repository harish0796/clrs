def binary_search(A, p, q, key):
    if p == q: return None
    r = int((p+q)/2)
    print(r , A[r])
    if A[r] == key:
        return r
    elif key < A[r]:
        return binary_search(A, p, r, key)
    else:
        return binary_search(A, r, q, key)
    

A = [1, 3 , 5 , 7 , 9 , 11]

index = binary_search(A,0,len(A), 0)

print(index)

""" The recurrence relation is T(n) = T(n/2) + O(1),
    by solving the reccurence, we get T(n) = O(logn) """

