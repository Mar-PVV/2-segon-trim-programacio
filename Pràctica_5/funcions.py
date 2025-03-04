import csv

def llegir_registre(nom_file):
    registre = []
    with open('./Pràctica_5/registres/{nom_file}.csv','r') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index > 1:
                registre.append([int(row[1]),int(row[2])])
    return registre

def escriure_registre(nom_file, registre):
    with open(f'./Pràctica_5/registres/{nom_file}.csv','w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',')
        for index, row in enumerate(registre):
            if index == 0:
                fila = ['num_monedes','treure1','treure2']
                csv_writer.writerow(fila)
            else:
                fila = [index,row[0],row[1]]
                csv_writer.writerow(fila)

def crear_registre(nom_file, num_monedes):
    registre = []

    # Crear taula de 0 de registre.
    for i in range(num_monedes+1):
        registre.append([0,0])
    
    escriure_registre(nom_file, registre)
