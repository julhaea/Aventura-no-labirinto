"""
Aventura no Labirinto

Este pacote contém os módulos necessários para o jogo "Aventura no Labirinto", 
onde o jogador explora um labirinto interagindo através do terminal.

Módulos:
- labirinto_txt: Cria o mapa do labirinto em forma de lista.
- labirinto: Funções para criar e imprimir o labirinto.
- jogador: Controle das ações do jogador no labirinto.
- utils: Impressão de instruçõese página de vitória.
"""

# Importa os módulos do pacote
from . import labirinto_txt
from . import labirinto
from . import jogador
from . import utils
