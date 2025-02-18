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

    for divisor in llista1:
        if divisor not in llista2:
            mcm = mcm * divisor

    for divisor in llista2:
        if divisor not in llista1:
            mcm = mcm * divisor
        else:
            exp1 = llista1.count(divisor)
            exp2 = llista2.count(divisor)
            exp = max(exp1,exp2)
            mcm = mcm * divisor**exp
            
    return mcm


def calcul_MCD(num1, num2):
  
    llista1 = factoritzacio_primers(num1)
    llista2 = factoritzacio_primers(num2)

    
    llista_mcd = []
    for factor in llista1:
        if factor in llista2:
            llista_mcd.append(factor)
            llista2.remove(factor)  


    mcd = 1
    for factor in llista_mcd:
        mcd *= factor
    return mcd
