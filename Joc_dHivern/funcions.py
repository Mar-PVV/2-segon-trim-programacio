from escenaris import entrada, passadis, biblioteca, soterrani, habitacio_secreta, cuina

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
        escenari_actual = cuina
        print("\nEntres a la cuina.")
    elif accio == "3":
        escenari_actual = biblioteca
        print("\nLa porta del final porta a la biblioteca.")
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
            print("\Trobes una porta secreta. Està tancada. Potser necessites alguna cosa per obrir-la.")
    elif accio == "5":
        print("\nTornes al passadis.")
        escenari_actual = passadis
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

def accions_cuina(accio, inventari):
    escenari_actual = cuina
    if not "ploms on" in inventari:
        print("Ups! No veus res de res... Has de tornar enrrere.")
        escenari_actual = passadis
    else:
        if accio == "1":
            mostrar_inventari(inventari)
        elif accio == "2":
            if "foc" not in inventari:
                print("\nEncens la llar de foc. La cuina ara està càlida.")
                inventari.append("foc")
            else:
                print("\nApagues el foc. Brrrr quin fred!")
                inventari.remove("foc")
        elif accio == "3":
            if "foc" in inventari:
                print("Quanta escalfor! Aparta aparta!")
            else:
                print("\nExamineu la llar de foc, i trobes una clau gran.")
                inventari.append("clau gran")
        elif accio == "4":
            print("\nSortiu de la cuina.")
            escenari_actual = passadis
        else:
            print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

def accions_soterrani(accio, inventari):
    escenari_actual = soterrani
    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        print("\nExplores el soterrani, i trobes que uns ploms estan abaixats, els apuges.")
        inventari.append("ploms on")
    elif accio == "3":
        if "clau gran" in inventari:
            print("\nExlores i trobes una porta secreta! L'obres amb la clau gran vas a parar a una habitació secreta.")
            escenari_actual = habitacio_secreta
        else:
            print("\nExlores i trobes una porta secreta! Eps! Està tancada! Necessites una clau gran.")
    elif accio == "4":
        print("\nDecideixes sortir del soterrani i tornar al passadís.")
        escenari_actual = passadis
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

def accions_habitacio_secreta(accio, inventari, intents):
    escenari_actual = habitacio_secreta
    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        print("\nExplores la caixa forta, però sembla que necessites un codi per obrir-la.")
        if intents > 0:
            codi = input("Codi: ")
            if codi == "4421":
                print("\nExplores la caixa forta, i trobes un REGAL! Bones festes a tots! -Mar")
                exit()
            else:
                intents -= 1
                print(f"Codi erroni... Et queden {intents} intents.")
        else:
            print("Caixa forta bloquejada.")
            exit()

    elif accio == "3":
        print("\nExplores l'habitació i trobes uns nombres apuntats a un paper, 4421.")
    elif accio == "4":
        print("\nDecideixes sortir de l'habitació secreta.")
        escenari_actual = soterrani
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari, intents
