import emoji
from . import labirinto_txt

def criar_labirinto():
    """
    Cria o labirinto nesse módulo.

    A função carrega o mapa do labirinto a partir do módulo labirinto_txt 
    e retorna uma lista representando o mapa.

    Retorna:
        labirinto (lista): Uma lista contendo as linhas do labirinto.
    """
    labirinto = labirinto_txt.labirinto
    return labirinto

def imprimir_labirinto(labirinto, jogador_posicao):
    """
    Imprime o labirinto no terminal com o jogador na posição atual.

    Parâmetros:
        labirinto (lista): Mapa do labirinto em forma de lista, onde cada elemento é uma linha.
        jogador_posicao (tupla): Tupla com as coordenadas (linha, coluna) da posição atual do jogador.

    A função percorre o mapa do labirinto e imprime cada linha, substituindo 
    a célula correspondente à posição do jogador por um emoji de quadrado azul (representando o jogador).
    """
    print('              ')  # Espaçamento para a impressão
    for i, linha in enumerate(labirinto):
        linha_str = ''
        for j, celula in enumerate(linha):
            if (i, j) == jogador_posicao:
                linha_str += emoji.emojize(':blue_square:')  # Representa a posição do jogador
            else:
                linha_str += celula  # Imprime a célula original do labirinto
        
        if i == 10:
            print(linha_str)  # Imprime a última linha
        else:
            print(linha_str)  # Imprime as demais linhas
