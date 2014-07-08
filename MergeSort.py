'''
Created on 2014/7/8

@author: zarey
'''

def merge(A, p, q, r):
    L = A[ :p ]
    R = A[ p+1: ]
    i, j, k = 0, 0, 0
    for k in range(r - p):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r)/2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

if __name__ == '__main__':
    elements = [3,7,0,6,1,9,8,5,2,4]
    merge_sort(elements)
    print elements