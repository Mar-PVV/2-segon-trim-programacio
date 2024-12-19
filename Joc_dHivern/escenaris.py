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
    """
)

passadis = Escenari(
    "Passadís",
    "Has obert la porta i ara ets en un passadís llarg. Hi ha un cofre tancat amb clau i una porta al final.",
    {
        "1": "Consultar inventari",
        "2": "Anar a la porta de l'esquerra",
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

habitacio_secreta = Escenari(
    "Habitació Secreta",
    "Has trobat una habitació secreta! Al centre, hi ha una caixa forta tancada amb cadenat. Potser necessitaràs alguna cosa per obrir-la.",
    {
        "1": "Consultar inventari",
        "2": "Examinar la caixa forta",
        "3": "Examinar habitació secreta",
        "4": "Sortir de l'habitació secreta"
    },
    """
    +-----------------------+
    |                       |
    |    [ Caixa Forta ]    |
    |                       |
    |                       |
    |                       |
    +-----------------------+
    """
)

biblioteca = Escenari(
    "Biblioteca",
    "Ets a la biblioteca. Hi ha llibres per tot arreu. Un llibre estrany sembla tenir alguna cosa amagada.",
    {
        "1": "Consultar inventari",
        "2": "Examinar els llibres",
        "3": "Obrir el llibre estrany",
        "4": "Examinar estanteria de llibres",
        "5": "Tornar al passadis"
    },
    """
    """
)

cuina = Escenari(
    "Cuina",
    "",
    {
        "1": "Consultar inventari",
        "2": "Encendre/apagar el foc",
        "3": "Examinar llar de foc",
        "4": "Sortir de la cuina"
    },
    """
    """
)

soterrani = Escenari(
    "Soterrani",
    "Estàs al soterrani. La porta secreta s'ha obert, i ara veus un camí més fosc que porta a una altra sortida.",
    {
        "1": "Consultar inventari",
        "2": "Examinar a la dreta del soterrani",
        "3": "Examinar a l'esquerra del soterrani",
        "4": "Sortir del soterrani"
    },
    """
    """
)
