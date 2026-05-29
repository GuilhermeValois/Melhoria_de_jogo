import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.columns import Columns


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

def distribuição_pontos(heroi,ataque_heroi,defesa_heroi,bonus_heroi,vilao,ataque_vilao,defesa_vilao,bonus_vilao):
    console = Console()

    tabela_heroi = Table(title = f"🔵 {heroi.nome} ")
    tabela_heroi.add_column("Atributos",)
    tabela_heroi.add_column("Pontos")

    tabela_heroi.add_row("⚔️  Dano", f"{ataque_heroi}")
    tabela_heroi.add_row("🛡️  Defesa", f"{defesa_heroi}")
    tabela_heroi.add_row("✨ Bônus", f"{bonus_heroi}")

    tabela_vilao = Table(title = f"🔴 {vilao.nome} ")
    tabela_vilao.add_column("Atributos",)
    tabela_vilao.add_column("Pontos")

    tabela_vilao.add_row("⚔️  Dano", f"{ataque_vilao}")
    tabela_vilao.add_row("🛡️  Defesa", f"{defesa_vilao}")
    tabela_vilao.add_row("✨ Bônus", f"{bonus_vilao}")

    ' '

    
    
    console.print(Columns([tabela_heroi, tabela_vilao], align = "center"))
    