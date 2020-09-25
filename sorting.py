import math
import numpy as np

from random import randint

def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    # Create lists
    L = list()
    R = list()
    for i in range(p, q+1):
        L.append(A[i])
    for i in range(q+1, r+1):
        R.append(A[i])
    # Sentinal values
    L.append(math.inf)
    R.append(math.inf)

    # Merge runs
    try:
        i, j = 0, 0
        for k in range(p, r+1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
    except IndexError as e:
        raise(e)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        k = randint(0, len(arr)-1)
        working = list(arr[:k]) + list(arr[k+1:])
        left = [i for i in working if i <= arr[k]]
        right = [i for i in working if i > arr[k]]
        return quicksort(left) + [arr[k]] + quicksort(right)


def main():
    # Generate random array for testing
    A = np.random.randint(0, 50, size=15)
    print(A)

    # Test sorting them
    # merge_sort(A, 0, len(A)-1)
    A = quicksort(A)
    print(A)


if __name__ == "__main__":
    main()

