'''
Created on 2014/7/8

@author: zarey
'''

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while A[i] > key and i >= 0:
            A[i+1] = A[i]         
            i -= 1
        A[i+1] = key

if __name__ == '__main__':
    elements = [3,7,0,6,1,9,8,5,2,4]
    insertion_sort(elements)
    print elements