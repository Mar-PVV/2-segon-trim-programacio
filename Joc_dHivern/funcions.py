from escenaris import entrada, passadis, biblioteca, soterrani, habitacio_secreta

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
    elif accio == "3":
        print("\nLa porta del final està tancada amb un cadenat. Necessites la clau adequada.")
    elif accio == "4":
        print("\nTornes a l'entrada.")
        escenari_actual = entrada
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

def accions_biblioteca(accio, inventari):
    escenari_actual = biblioteca
    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        print("\nExplores els llibres. Un llibre sembla una mica estrany...")
    elif accio == "3":
        if "llibre clau" not in inventari:
            print("\nTrobes un llibre antic que amaga una clau!")
            inventari.append("llibre clau")
        else:
            print("\nJa tens el llibre amb la clau.")
    elif accio == "4":
        if "llibre clau" in inventari:
            print("\nObres una porta secreta amagada dins de la biblioteca.")
            escenari_actual = soterrani
        else:
            print("\nLa porta secreta està tancada. Potser necessites alguna cosa per obrir-la.")
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

def accions_cuina(accio, inventari):
    escenari_actual = cuina
    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        if "foc" in inventari:
            print("\nEncens la llar de foc. La cuina ara està càlida.")
        else:
            print("\nNecessites un encenedor o alguna cosa per encendre el foc.")
    elif accio == "3":
        print("\nExamineu la llar de foc, i us adoneu que és antiga però funcional.")
    elif accio == "4":
        print("\nSortiu de la cuina.")
        escenari_actual = soterrani
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

def accions_soterrani(accio, inventari):
    escenari_actual = soterrani
    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        print("\nExplores el soterrani, però no trobes res interessant.")
    elif accio == "3":
        if "cadenat" in inventari:
            print("\nObres una porta secreta al soterrani amb el cadenat.")
            escenari_actual = cuina
        else:
            print("\nLa porta al soterrani està tancada amb cadenat. Necessites una clau.")
    elif accio == "4":
        print("\nDecideixes sortir del soterrani i tornar al passadís.")
        escenari_actual = passadis
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

def accions_habitacio_secreta(accio, inventari):
    escenari_actual = habitacio_secreta
    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        print("\nExplores la caixa forta, però sembla que necessites una clau per obrir-la.")
    elif accio == "3":
        if "llibre clau" in inventari:
            print("\nObres la caixa forta amb la clau que vas trobar al llibre.")
            inventari.append("regal")
            print("\nHas trobat un regal! Felicitats!")
            escenari_actual = None  # El joc es termina aquí
        else:
            print("\nLa caixa forta segueix tancada. Potser necessites la clau correcta.")
    elif accio == "4":
        print("\nDecideixes sortir de l'habitació secreta.")
        escenari_actual = passadis
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari
