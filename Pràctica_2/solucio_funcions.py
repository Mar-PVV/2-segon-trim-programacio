def iteracions_MCD_Euclides(a,b):
    iteracions = 0

    a = max(a, b)
    b = min(a,b)

    while b != 0:
        r = a % b

        a = b
        b = r
        iteracions += 1

    return iteracions