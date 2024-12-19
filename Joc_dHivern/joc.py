from funcions import accions_biblioteca, accions_cuina, accions_habitacio_secreta, accions_passadis, accions_entrada, accions_soterrani
from escenaris import entrada, passadis, cuina, soterrani, biblioteca, habitacio_secreta

# Funció principal del joc
def joc():
    escenari_actual = entrada
    inventari = []
    intents = 3

    while True:
        escenari_actual.mostra()
        accio = input("\nQuè vols fer? ")

        # Gestió de les accions a l'entrada
        if escenari_actual == entrada:
            escenari_actual, inventari = accions_entrada(accio, inventari)
            
        # Gestió de les accions al passadís
        elif escenari_actual == passadis:
            escenari_actual, inventari = accions_passadis(accio, inventari)

        elif escenari_actual == soterrani:
            escenari_actual, inventari = accions_soterrani(accio, inventari)

        elif escenari_actual == cuina:
            escenari_actual, inventari = accions_cuina(accio, inventari)

        elif escenari_actual == biblioteca:
            escenari_actual, inventari = accions_biblioteca(accio, inventari)
        else:
            escenari_actual, inventari, intents = accions_habitacio_secreta(accio, inventari, intents)

        input("\nPrem Enter per continuar...")

# Inicia el joc
joc()
