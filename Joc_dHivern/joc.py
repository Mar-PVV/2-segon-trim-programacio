from funcions import accions_passadis, accions_entrada
from escenaris import entrada, passadis

# Funció principal del joc
def joc():
    escenari_actual = entrada
    inventari = []

    while True:
        escenari_actual.mostra()
        accio = input("\nQuè vols fer? ")

        # Gestió de les accions a l'entrada
        if escenari_actual == entrada:
            escenari_actual, inventari = accions_entrada(accio, inventari)
            
        # Gestió de les accions al passadís
        elif escenari_actual == passadis:
            escenari_actual, inventari = accions_passadis(accio, inventari)

        input("\nPrem Enter per continuar...")

# Inicia el joc
joc()
