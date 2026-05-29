import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import emoji

def limpar():
    os.system('cls')

def titulo_combate():

    console = Console()
    console.print(Panel(Align.center("A batalha começou!"), title = "⚔️ COMBATE⚔️", border_style = "red"))

def titulo_História(heroi, vilao):

    console = Console()
    console.print(Panel(Align.center(f"{heroi.nome} VS {vilao.nome}"), title = "HISTÓRIA", border_style = "yellow"))

def status(personagem1,personagem2):

    console = Console()
    tamanho = 20

    preenchido1 = int((personagem1.vida / personagem1.vida_max) * tamanho)

    preenchido2 = int((personagem2.vida / personagem2.vida_max) * tamanho)
    barra1 = "█" * preenchido1
    barra2 = "█" * preenchido2
    vazio1 = "-" * (tamanho - preenchido1)
    vazio2 = "-" * (tamanho - preenchido2)

    console.print(Panel(Align.center(f"{personagem1.nome}:[{barra1}{vazio1}] {personagem1.vida}/{personagem1.vida_max} PTS: {personagem1.pontos} DANO: {personagem1.dano}  {personagem2.nome}:[{barra2}{vazio2}] {personagem2.vida}/{personagem2.vida_max} PTS: {personagem2.pontos} DANO: {personagem2.dano}"), title = "STATUS", border_style = "blue"))

def istribuição_pontos(heroi,ataque_heroi,defesa_heroi,bonus_heroi,vilao,ataque_vilao,defesa_vilao,bonus_vilao):
    console = Console()
    Painel1 = Panel(Align.center(f"{heroi.nome}:\nAtaque:{ataque_heroi}\nDefesa:{defesa_heroi}\nBônus:{bonus_heroi}\n\n{vilao.nome}:\nAtaque:{ataque_vilao}\nDefesa:{defesa_vilao}\nBônus:{bonus_vilao}"), border_style = "red")
    Painel2 = Panel(Align.center(f"{vilao.nome}:\nAtaque:{ataque_vilao}\nDefesa:{defesa_vilao}\nBônus:{bonus_vilao}\n\n{heroi.nome}:\nAtaque:{ataque_heroi}\nDefesa:{defesa_heroi}\nBônus:{bonus_heroi}"), border_style = "green")
    console.print(Painel1)
    console.print(Painel2)