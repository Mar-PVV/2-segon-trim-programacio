def prime(x, y):
    prime_list = []
    for i in range(x, y+1):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

def factoritzacio_primers(num):
    llista_primers = prime(1,num)
    factors_primers = []

    for num_primer in llista_primers:
        if num != 1:
            while num % num_primer == 0:
                factors_primers.append(num_primer)
                num = num / num_primer
        else:
            break
    
    return factors_primers

def calcul_mcm(num1, num2):
    llista1 = factoritzacio_primers(num1)
    llista2 = factoritzacio_primers(num2)

    mcm = 1

    for factor in llista1:
        if factor not in llista2:
            mcm = mcm * factor
        else:

    

    # El mcm seran tots els factors comuns i no comuns i en cas de comuns els de major exponent.