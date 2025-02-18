import inspect as i
import sys

def mostrar_f(f):
    sys.stdout.write(i.getsource(f))

def f(x):
    return  x ** 2 + 5 * x + 6 

def compleix_bolzano(f, a, b):
    return f(a) * f(b) < 0

def biseccio(f, a, b, tol):
    iteracions = 0
    valor_mig = (a + b) / 2 

    while abs(f(valor_mig)) > tol:

        if f(valor_mig) * f(a) > 0:
            a = valor_mig
        else:
            b = valor_mig

        valor_mig = (a + b) / 2 
        iteracions += 1    

    return valor_mig, f(valor_mig), iteracions