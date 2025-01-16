def iteracions_MCD_Euclides(a,b):
    iteracions = 0

    if b < a:
        aux = b
        b = a
        a = aux

    # Manera alternativa:
    if b < a:
        nums = [a,b]
        b = min(nums)
        a = max(nums)

    # Programa while Euclides

    return iteracions