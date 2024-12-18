import os

# Funció per netejar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Classe per representar un escenari
class Escenari:
    def __init__(self, nom, descripcio, opcions, ascii_art):
        self.nom = nom
        self.descripcio = descripcio
        self.opcions = opcions
        self.ascii_art = ascii_art

    def mostra(self):
        clear_screen()
        print(self.ascii_art)
        print(f"\n{self.descripcio}\n")
        for clau, text in self.opcions.items():
            print(f"{clau}: {text}")

# Definim els escenaris
entrada = Escenari(
    "Entrada",
    "Ets en una habitació fosca amb una porta tancada davant teu. Veus un calaix petit i una espelma apagada.",
    {
        "1": "Consultar inventari",
        "2": "Obrir el calaix",
        "3": "Encendre l'espelma",
        "4": "Anar a la porta"
    },
    """
    +---------+
    |         |
    |   [ ]   | <- Calaix
    |         |
    |   (_)   | <- Espelma
    |         |
    |   ===   | <- Porta
    +---------+
    """
)

passadis = Escenari(
    "Passadís",
    "Has obert la porta i ara ets en un passadís llarg. Hi ha un cofre tancat amb clau i una porta al final.",
    {
        "1": "Consultar inventari",
        "2": "Obrir el cofre",
        "3": "Anar a la porta del final",
        "4": "Tornar a l'entrada"
    },
    """
    +-----------------------+
    |                       |
    |    [ Cofre tancat ]   |
    |                       |
    |        Porta          |
    +-----------------------+
    """
)