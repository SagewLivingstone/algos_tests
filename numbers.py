def euclid(a: int, b: int):
    """
    use euclidian algorithm to compute gcd of a, b
    """
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def main():
    print(euclid(30, 21))
    print(euclid(21, 30))
    print(euclid(55, 45))

if __name__ == "__main__":
    main()
