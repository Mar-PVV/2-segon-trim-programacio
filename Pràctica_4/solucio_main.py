from solucio_funcions import f, compleix_bolzano, biseccio, mostrar_f

print('Donada la funció següent:')
mostrar_f(f)
a = float(input('Valor d\'A: '))
b = float(input('Valor de B: '))                                                               

while not compleix_bolzano(f,a,b):
    a = float(input('Valor d\'A: '))
    b = float(input('Valor de B: ')) 

tol = 1e-10
solucio, valor_funcio, iteracions = biseccio(f,a,b,tol)

print('Dades d\'entrada: ')
print('a = ' + str(a))
print('b = ' + str(b))
mostrar_f(f)
print('Tolerància = ' + str(tol) )
print('Dades de sortida')
print ('Solució = ' + str(solucio))
print('Valor de la funció = '  + str(valor_funcio))
print('Nombre d\'iteracions = ' + str(iteracions))