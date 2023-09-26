# megan.roxanne.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE

STYLE["width"] = 800
STYLE["height"] = "600px"

IMAGEM = "https://img.freepik.com/free-vector/retro-styled-pattern-background_1048-6593.jpg"
PORTAO_BRONZE = "https://precoimbativel.net/494016-large_default/portao-pedonal-philadelphia-em-aluminio-a-medida.jpg"
PALACIO_CORAL = "https://www.parquesdesintra.pt/media/trwbbkth/parques_de_sintra_palacio_de_queluz_hero_01.jpg?rxy=0.49833333333333335,0.405&width=750&height=750&quality=90&format=webp&rnd=132442512038670000"
PEAO = "https://lojagrow.vteximg.com.br/arquivos/ids/168597-1000-1000/Peao-Grow-Vermelho.png?v=637487474175630000"

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