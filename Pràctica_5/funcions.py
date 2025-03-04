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

def escriure_registre(registre):
    with open('./Pràctica_5/registre.csv','w') as f:
        csv_writer = csv.writer(f, delimiter='w')
        for index, row in enumerate(registre):
            csv_writer.writerow([index,row[0],row[1]])