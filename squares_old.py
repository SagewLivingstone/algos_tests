

def find_value_2d(A: list,
                  k: int,
                  x0: int,
                  y0: int,
                  x1: int,
                  y1: int):
    try:
        if x0 == x1 or y0 == y1:
            return None
        mx = int( (x0+x1)/2 )  # Midpoint
    except RecursionError as e:
        print(x0, y0)
        print(x1, y1)
        raise e
    my = int( (y0+y1)/2 )

    inv1 = set()
    inv2 = set()
    inv3 = set()
    inv4 = set()

    # Test all 4 points
    # Testing 1
    sx = int( (x0+mx)/2 )  # Sample coords
    sy = int( (y0+my)/2 )
    if k == A[sy][sx]:
        return (sy, sx)
    if k > A[sy][sx]:
        inv1.add(1)
    if k < A[sy][sx]:
        inv1.add(4)
        inv2.add(3)
        inv2.add(4)
        inv3.add(2)
        inv3.add(4)
        inv4.add(1)
        inv4.add(2)
        inv4.add(3)
        inv4.add(4)
    
    # Testing 2
    sx = int( (x1+mx)/2 )  # Sample coords
    sy = int( (y0+my)/2 )
    if k == A[sy][sx]:
        return (sy, sx)
    if k > A[sy][sx]:
        inv1.add(1)
        inv1.add(2)
        inv2.add(1)
    if k < A[sy][sx]:
        inv2.add(4)
        inv4.add(2)
        inv4.add(4)
    
    # Testing 3
    sx = int( (x0+mx)/2 )  # Sample coords
    sy = int( (y1+my)/2 )
    if k == A[sy][sx]:
        return (sy, sx)
    if k > A[sy][sx]:
        inv1.add(1)
        inv1.add(3)
        inv3.add(1)
    if k < A[sy][sx]:
        inv3.add(4)
        inv4.add(3)
        inv4.add(4)

    # Testing 1
    sx = int( (x1+mx)/2 )  # Sample coords
    sy = int( (y1+my)/2 )
    if k == A[sy][sx]:
        return (sy, sx)
    if k < A[sy][sx]:
        inv4.add(1)
    if k > A[sy][sx]:
        inv1.add(1)
        inv1.add(2)
        inv1.add(3)
        inv1.add(4)
        inv2.add(1)
        inv2.add(3)
        inv3.add(1)
        inv3.add(2)
        inv4.add(1)
    
    if len(inv1) < 4:
        f1 = find_value_2d(A, k, x0, y0, mx, my)
        if f1:
            return f1
    if len(inv2) < 4:
        f2 = find_value_2d(A, k, mx, y0, x1, my)
        if f2:
            return f2
    if len(inv3) < 4:
        f3 = find_value_2d(A, k, x0, my, mx, y1)
        if f3:
            return f3
    if len(inv4) < 4:
        f4 = find_value_2d(A, k, mx, my, x1, y1)
        if f4:
            return f4
    return None