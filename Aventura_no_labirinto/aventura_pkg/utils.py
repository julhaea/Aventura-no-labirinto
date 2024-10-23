from rich.console import Console
import emoji

console = Console()

def imprime_instrucoes(nome):
    """
    Imprime as instruções do jogo.

    Parâmetros:
        nome (str): O nome do jogador informado no argumento da execução.
    
    A função exibe as instruções de como jogar o "Aventura no Labirinto", 
    com comandos para movimentação, início e saída do jogo.
    """
    console.print(f"[bold cyan]Bem-vindo ao Aventura no Labirinto {nome}![/bold cyan]")
    console.print("Use as teclas para mover o jogador:")
    console.print("→ [bold]Setas do Teclado[/bold] para mover o personagem.")
    console.print("→ [bold]S[/bold] para iniciar o jogo.")
    console.print("→ [bold]Q[/bold] para sair do jogo.")

def vitoria(nome):
    """
    Imprime a página de vitória quando o jogador vence.

    Parâmetros:
        nome (str): O nome do jogador informado no argumento da execução.
    
    A função exibe uma mensagem de congratulação quando o jogador vence, 
    formatada com emojis de quadrados verdes, e uma mensagem personalizada com o nome do jogador.
    """
    a = emoji.emojize(":green_square:")
    print("\n\n" + 16*a)
    print(16*a)
    console.print(4*a + f"[bold] Parabéns {nome}![/bold]" + 4*a)
    print(16*a)
    print(16*a)
    print(3*a + ' VOCÊ VENCEU O JOGO ' + 3*a)
    print(16*a)
    print(16*a + '\n')
