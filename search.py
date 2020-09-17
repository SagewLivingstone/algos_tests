import math

def binary_search(A: list(), key: object) -> int:
    """
    search for element 'key' in list A
    """

    low = 0
    high = len(A) - 1
    
    c = 12

    while c > 0:
        c -= 1
        mid = math.floor((high - low) / 2 + low)

        if A[mid] == key:
            return mid
        else:
            if A[mid] < key:
                low = mid
            else:
                high = mid

        if high == low + 1:
            if A[high] == key:
                return high
            elif A[low] == key:
                return low
            return None


def main():
    A = [1, 2, 6, 8, 9, 11, 13, 22, 33, 44, 55, 66, 77]

    print(44, binary_search(A, 44))
    print(11, binary_search(A, 11))
    print(2, binary_search(A, 2))
    print(1, binary_search(A, 1))
    print(24, binary_search(A, 24))


if __name__ == "__main__":
    main()

