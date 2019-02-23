#Rewrite the merge with no sentinels

def merge(A, p , q , r):
    L = A[p:r]
    R = A[r:q]
    i,j,k = 0,0,p
    print(L,R)
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1
        
    if j < len(R):
        A[k:q] = R[j:len(R)]

    if i < len(L):
        A[k:q] = L[i:len(L)]

def merge_sort(A,p,q):
    #While slicing the array atleast have 1 element
    if q - p > 1: 
        r = int((p + q)/2)
        merge_sort(A,p,r)
        merge_sort(A,r,q)
        merge(A,p,q,r)
       
A = [8,7,6,5,4,3,2,1,2,9,2.5]
merge_sort(A,0,len(A))
print(A)
