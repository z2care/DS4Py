'''
Created on 2014/9/11

@author: zarey
'''

def quick_sort(A, l, r):
    if l < r:
        k = partation(A, l, r)
        quick_sort(A, l, k - 1)
        quick_sort(A, k + 1, r)

def partation(A, l, r):
    x = A[r]
    i = l - 1
    for j in range(l , r):
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    i = i + 1
    A[i], A[r] = A[r], A[i]
    return i

if __name__ == '__main__':
    elements = [3,7,0,6,1,9,8,5,2,4]
    quick_sort(elements, 0, len(elements)-1)
    print elements
