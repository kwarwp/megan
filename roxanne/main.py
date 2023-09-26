# megan.roxanne.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"

class IlhaProibida:
    def __init__(self):
        oceano = Cena(IMAGEM).vai()
        portao = Elemento(PORTAO_BRONZE, x=10, y=50,
        w=100, h=100, tit="Portão de Bronze", cena=oceano)
        palacio = Elemento(PALACIO_CORAL, x=120, y=50, w=100, h=100, cena=oceano)
        self.peao = Peao(oceano)

class Terreno:
    def __init__(self, local, posx, posy, oceano):
        self.local = Elemento(local, x=posx, y=posy, w=100, h= 100,
        cena=oceano)

class Peao:
    def __init__(self, oceano):
        self.peao = Elemento(PAWN, x=20, y=70, w=80, h= 80,
        cena=oceano, vai=self.move)
        
    def move(self, ev=None):
        self.peao.x = 170
        
IlhaProibida()