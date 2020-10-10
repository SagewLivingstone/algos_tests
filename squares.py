from math import floor
from random import randint


def find_value_2d_div(A, x, l, r, u, d):
    """
    find value x in 2d arr A
    """
    # print(x, l, r, u, d)
    u_shelf = u
    for i in range(u, d+1):
        if x > A[i][l] and x > A[i][r]:
            u_shelf = i
        else:
            break
    d_shelf = d
    for i in range(d, u-1, -1):
        if x < A[i][r] and x < A[i][l]:
            d_shelf = i
        else:
            break

    if u_shelf >= d_shelf:
        return None

    if u_shelf + 1 <= d_shelf:
        return (u_shelf+1, A[u_shelf+1].index(x))  # Standin for binary search here

    # Not found but possible space, split in two:
    m = floor((l+r)/2)

    return find_value_2d_div(A, x, l, m, u_shelf, d_shelf) or find_value_2d_div(A, x, m+1, r, u_shelf, d_shelf)


def main():
    arr = [[i + 10*j for i in range(0, 10)] for j in range(0, 10)]
    for i in range(0, 10):
        print(arr[i])

    key = randint(0, 120)
    print("looking for:", key)

    print(find_value_2d_div(arr, key, 0, 9, 0, 9))


if __name__ == "__main__":
    main()
