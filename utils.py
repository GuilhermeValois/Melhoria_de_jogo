import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.progress_bar import ProgressBar
import emoji

def limpar():
    os.system('cls')

def titulo_combate():

    console = Console()
    console.print(Panel(Align.center("A batalha começou!"), title = "⚔️ COMBATE⚔️", border_style = "red"))

def status(personagem):
    tamanho = 20

    preenchido = int((personagem.vida / personagem.vida_max) * tamanho)

    barra = "█" * preenchido
    vazio = "-" * (tamanho - preenchido)

    print(f"[{barra}{vazio}] {personagem.vida}/{personagem.vida_max}  PONTOS: {personagem.pontos}")
