import csv

def llegir_registre():

    with open('./Pràctica_5/registre.csv','r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

llegir_registre()

def escriure_registre():
    pass