import inspect as i
import sys

def mostrar_f(f):
    sys.stdout.write(i.getsource(f))

