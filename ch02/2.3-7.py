""" Describe an O(nlgn) time algorithm that, given a set S of n integers and
another integer x, determines whether or not there exist two elements in S
whose sum is exactly x. """

def findPair(S, x):
    S.sort() #Takes O(nlogn)
    i, j = 0, len(S)-1
    while i < j:
        if S[i] + S[j] == x:
            return True
        elif S[i] + S[j] > x:
            j-=1
        else:
            i+=1
    return False
S = [3, 5, 6, 8, 5, 7, 9, 2, 1, 0]
x = 20

print(findPair(S,x))



