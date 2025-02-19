def iteracions_MCD_Euclides(x,y):
    iteracions = 0

    a = max(x,y)
    b = min(x,y)

    while b != 0:
        r = a % b

        a = b
        b = r
        iteracions += 1

    return iteracions