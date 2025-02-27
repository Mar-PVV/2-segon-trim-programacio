import random

num_monedes = 7
registre = []

# Crear taula de 0 de registre.
for i in range(num_monedes):
    registre.append([0,0])

print(registre)

monedes_restants = num_monedes
guanyador = None

print(f'[ {monedes_restants} monedes ]')

while monedes_restants > 0:

    monedes_usuari = int(input(f'Queden {monedes_restants} monedes, quantes en vols treure? 1 o 2? '))
    
    while monedes_restants - monedes_usuari < 0 or monedes_usuari not in [1,2]:
        monedes_usuari = int(input(f'Torna a provar.'))

    monedes_restants -= monedes_usuari
    print(f'[ {monedes_restants} monedes ]')

    if monedes_restants == 0:
        guanyador = 'usuari'
        print(f'Ha guanyat l\'{guanyador}')
        break

    treure_1 = registre[monedes_restants-1][0]
    treure_2 = registre[monedes_restants-1][1]

    if (treure_1 == 1 and treure_2 == 0) and monedes_restants > 1:
        monedes_restants -= 2
        print('L\'ordinador treu 2 monedes.')
    elif (treure_1 == 0 and treure_2 == 1) or monedes_restants == 1:
        monedes_restants -= 1
        print('L\'ordinador treu 1 moneda.')
    else:
        monedes_ordinador = random.randint(1,2)
        monedes_restants -= monedes_ordinador
        print(f'L\'ordinador treu {monedes_ordinador} monedes (aleatori).')

    print(f'[ {monedes_restants} monedes ]')
    
    if monedes_restants == 0:
        guanyador = 'ordinador'
        print(f'Ha guanyat l\'{guanyador}')
        break