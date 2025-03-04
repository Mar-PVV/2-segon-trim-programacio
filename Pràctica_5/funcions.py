import csv

def llegir_registre():
    registre = []
    with open('./Pràctica_5/registre.csv','r') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index > 1:
                registre.append([row[1],row[2]])
    return registre

print(llegir_registre())

def escriure_registre():
    pass