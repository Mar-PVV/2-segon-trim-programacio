import random

num_monedes = 7
registre = []

for i in range(num_monedes):
    registre.append([0,0])

print(registre)

monedes_restants = num_monedes
guanyador = None

while monedes_restants > 0:
    monedes_usuari = int(input(f'Queden {monedes_restants} monedes, quantes en vols treure? 1 o 2? '))

    monedes_restants -= monedes_usuari
    if monedes_restants == 0:
        guanyador = 'usuari'
        break

    # Mirar que si només queda una moneda, l'ordinador o l'usuari  no en tregui 2.
    if registre[monedes_restants-1][0] == 1 and registre[monedes_restants-1][1] == 0:
        monedes_restants -= 2
    elif registre[monedes_restants-1][0] == 0 and registre[monedes_restants-1][1] == 1:
        monedes_restants -= 1
    else:
        monedes_restants -= random.randint(1,2)
    
    if monedes_restants == 0:
        guanyador = 'ordinador'
        break