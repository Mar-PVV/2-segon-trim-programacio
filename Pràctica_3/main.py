from funcions import genera_llista, compta_repeticions, ordena_manual


rang = 3 # Els nombres poden anar de l'1 al 3.
longitud = 5 # La llista estarà composta per 5 elements.

llista = genera_llista(rang, longitud)

print(f'La llista inicial és: {llista}')

llista_elements, num_repeticions = compta_repeticions(llista)

print(f'Elements que formen la llista: {llista_elements}')
print(f'Nombre de repeticions de cada element de la llista: {num_repeticions}')

llista_ordenada = ordena_manual(llista_elements)

print(f'Llista d\'elements ordenada: {llista_ordenada}')

llista_ordenada = ordena_manual(llista)

print(f'Llista ordenada: {llista_ordenada}')
