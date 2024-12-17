def prime(x, y):
    prime_list = []
    for i in range(x, y):
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
    llista_primers = prime(1,num) # Us retorna per exemple: [2,3,5,7,11]
    
    # Calcular llista de factors primers