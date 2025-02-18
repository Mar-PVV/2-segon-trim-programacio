import random

def genera_llista(rang, longitud): 
    llista = []
    for i in range(longitud):
        llista.append(random.randint(1,rang))
    return llista

def compta_repeticions(llista):
    elements = []
    recompte = []

    for element in llista:
        if element not in elements:
            num_repeticions = 0
            for element2 in llista:
                if llista[element2] == element:
                    num_repeticions += 1
            elements.append(element)
            recompte.append(num_repeticions)

    return elements, recompte

def ordena_manual(llista):
  
    for element in llista:
        for i in range(len(llista)-1):
            if llista[i] > llista[i + 1]:
                aux = llista[i]  
                llista[i] = llista[i + 1]
                llista[i + 1]  = aux
                
    return llista
