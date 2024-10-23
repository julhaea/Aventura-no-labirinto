import argparse
from aventura_pkg import labirinto, jogador, utils
import pynput.keyboard

def iniciar_jogo(nome):
    """Função que inicializa o jogo.
    
    Parâmetros: 
        Nome: recebe o nome declarado no argumento da execução"""
    utils.imprime_instrucoes(nome)
    lab = labirinto.criar_labirinto()
    jogador_pos, situacao = jogador.iniciar_jogador()
    
    def on_press(tecla):
        nonlocal jogador_pos, situacao  # Permite modificar as variáveis da função externa
        if hasattr(tecla, 'char') and tecla.char == "q":
            print("Saindo do jogo...")
            return False  # Para o listener
        
        # Movimento do jogador (defina as teclas adequadas para o seu jogo)
        if tecla == pynput.keyboard.Key.up:
            jogador_pos = jogador.mover(jogador_pos, lab, 'w')
        elif tecla == pynput.keyboard.Key.down:
            jogador_pos = jogador.mover(jogador_pos, lab, 's')
        elif tecla == pynput.keyboard.Key.left:
            jogador_pos = jogador.mover(jogador_pos, lab, 'a')
        elif tecla == pynput.keyboard.Key.right:
            jogador_pos = jogador.mover(jogador_pos, lab, 'd')
        
        # Atualiza a pontuação e imprime o labirinto
        situacao += jogador.situar(jogador_pos, lab)
        labirinto.imprimir_labirinto(lab, jogador_pos)

        # Verifica se o jogador venceu
        if situacao ==True:
            utils.vitoria(nome)
            return False  # Para o listener



    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join() 


def main():
    """Inicializa a execução do código."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True, help="Nome do(a) jogador(a)")
    
    args = parser.parse_args()

    iniciar_jogo(args.name)

main()