import emoji

def iniciar_jogador():
    """
    Inicia o jogador na posição inicial e define a condição de vitória como falsa.

    Retorna:
    --------
    tupla: 
        Retorna a posição inicial do jogador como uma tupla (x, y) com (0, 0).
    bool: 
        Retorna False para indicar que o jogador ainda não venceu.
    """
    return (0, 0), False

def mover(posicao_atual, labirinto, tecla):
    """
    Move o jogador dentro do labirinto baseado na tecla pressionada, se o espaço estiver livre.

    Parâmetros:
    posicao_atual: tupla
        A posição atual do jogador no formato (x, y).
    labirinto: lista
        O mapa do labirinto, representado como uma matriz 2D de listas.
    tecla: str
        Recebe 'w', 's', 'a' ou 'd' para indicar respectivamente as teclas para cima, baixo, esquerda ou direita.

    Retorna:
    tupla:
        A nova posição do jogador após o movimento, no formato (x, y).
    
    Regras:
    - 'w': Move para cima, se estiver livre.
    - 's': Move para baixo, se estiver livre.
    - 'a': Move para a esquerda, se estiver livre.
    - 'd': Move para a direita, se estiver livre.
    - O jogador só pode se mover se o espaço de destino não estiver ocupado por um bloco laranja.
    """
    x, y = posicao_atual
    match tecla:
        case 'w' if x > 0 and labirinto[x-1][y] != emoji.emojize(":orange_square:"):
            x -= 1
        case 's' if x < len(labirinto) - 1 and labirinto[x+1][y] != emoji.emojize(":orange_square:"):
            x += 1
        case 'a' if y > 0 and labirinto[x][y-1] != emoji.emojize(":orange_square:"):
            y -= 1
        case 'd' if y < len(labirinto[0]) - 1 and labirinto[x][y+1] != emoji.emojize(":orange_square:"):
            y += 1

    return (x, y)


def situar(jogador_posicao, labirinto):
    """
    Verifica a condição de vitória do jogador.

    Parâmetros:
    jogador_posicao: tupla
        A posição atual do jogador no formato (x, y).
    labirinto: lista
        O mapa do labirinto, em formato de listas.

    Retorna:
    bool:
        Retorna True se o jogador atingir o bloco verde no final do labirinto,
        indicando que o jogador venceu. Caso contrário, retorna False.
    """
    if labirinto[jogador_posicao[0]][jogador_posicao[1]] == emoji.emojize(":green_square:"):
        return True
    else:
        return False
