import pandas as pd

def llegir_registre():
    file = pd.read_csv('registre.csv')
    
    registre = []
    next(file)

    for i in file:
        registre.append([i[1],i[2]])

    print(registre)

def escriure_registre():
    pass