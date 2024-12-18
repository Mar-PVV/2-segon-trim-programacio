from escenaris import entrada, passadis

def mostrar_inventari(inventari):
    if len(inventari) == 0:
        print("Ops! Tens l'inventari buit...")
    else:
        print("Això és el que tens ara mateix a l'inventari!")
        for element in inventari:
            print('\t' + element)

def accions_entrada(accio, inventari):
    escenari_actual = entrada
    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        if "clau petita" not in inventari:
            print("\nTrobes una clau petita dins del calaix!")
            inventari.append("clau petita")
        else:
            print("\nEl calaix està buit.")
    elif accio == "3":
        if "encenedor" in inventari:
            print("\nEncens l'espelma. Ara l'habitació està il·luminada.")
        else:
            print("\nNecessites un encenedor per encendre l'espelma.")
    elif accio == "4":
        if "clau petita" in inventari:
            print("\nObres la porta amb la clau petita i entres al passadís.")
            escenari_actual = passadis
        else:
            print("\nLa porta està tancada amb clau.")
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

def accions_passadis(accio, inventari):
    escenari_actual = passadis
    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        if "clau gran" in inventari:
            print("\nObres el cofre i trobes un encenedor!")
            inventari.append("encenedor")
        else:
            print("\nEl cofre està tancat amb clau. Necessites una clau gran.")
    elif accio == "2":
        print("\nLa porta del final està tancada amb un cadenat. Necessites la clau adequada.")
    elif accio == "3":
        print("\nTornes a l'entrada.")
        escenari_actual = entrada
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari