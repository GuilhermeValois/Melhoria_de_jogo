from personagem import Personagem
from heroi import Heroi
from vilao import Vilao
import random


def main():
    # Criando personagens e vilões
    heroi = Heroi('Heroi', 30, 100, 12, 2)
    vilao = Vilao('Conquista', 45, 120, 'Alta', 15, 2)
    while True:
        heroi_nome = input("Digite o nome do herói: ")
        if heroi_nome:
            heroi = Heroi(heroi_nome, 30, 100, 12, 2)
            break

    ataque_heroi = 0
    defesa_heroi = 0
    bonus_heroi = 0
    print(f"\nVocê enfrentará o vilão {vilao.nome}.")
    while True:

        if heroi.vida <= 0:
            print(f"\n{heroi.nome} foi derrotado por {vilao.nome}!")
            break
        if vilao.vida <= 0:
            print(f"\n{vilao.nome} foi derrotado por {heroi.nome}!")
            break

        print(f"\nVida de {heroi.nome}: {heroi.vida}////Vida de {vilao.nome}: {vilao.vida}")
        print(f"Pontos de {heroi.nome}: {heroi.pontos}/////Pontos de {vilao.nome}: {vilao.pontos}")

        while True:
            try:
                ataque_heroi = int(input(f"\nDigite a força do ataque (0-{heroi.pontos}): "))
                if 0 <= ataque_heroi <= heroi.pontos:
                    heroi.pontos -= ataque_heroi
                    break
                else:
                    print(f"Valor inválido! Digite um número entre 0 e {heroi.pontos}.")
                    continue
            except ValueError:
                print("Entrada inválida! Por favor, digite um número inteiro.")
                continue
           
        if 0 != heroi.pontos:
            while True:
                try:
                    defesa_heroi = int(input(f"Digite a força da defesa (0-{heroi.pontos}): "))
                    if 0 <= defesa_heroi <= heroi.pontos:
                        heroi.pontos -= defesa_heroi
                        break
                    else:
                        print(f"Valor inválido! Digite um número entre 0 e {heroi.pontos}.")
                        continue
                except ValueError:
                    print("Entrada inválida! Por favor, digite um número inteiro.")
                    continue

        if 0 != heroi.pontos:
            bonus_heroi = heroi.pontos
        
        heroi.pontos = 2 + bonus_heroi

        ataque_vilao = random.randint(0, vilao.pontos)
        defesa_vilao = random.randint(0, vilao.pontos - ataque_vilao)
        bonus_vilao = vilao.pontos - ataque_vilao - defesa_vilao

        vilao.pontos = 2 + bonus_vilao

        Ataque_final_heroi = ataque_heroi - defesa_vilao
        Ataque_final_vilao = ataque_vilao - defesa_heroi
        if Ataque_final_heroi < 0:
            Ataque_final_heroi = 0
        if Ataque_final_vilao < 0:
            Ataque_final_vilao = 0

        heroi.ataque(vilao, Ataque_final_heroi)
        print(f"{heroi.nome} se defendeu com {defesa_heroi} pontos!")
        vilao.ataque(heroi, Ataque_final_vilao)
        print(f"{vilao.nome} se defendeu com {defesa_vilao} pontos!")

        
        
       

    # Mostrando personagens
    print(heroi)
    print(vilao)

    # Vilão ataca o herói
    vilao.ataque(heroi)

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)
    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

    # Mudando nome do NPC
    npc.update_nome('Princesa Zelda')
    print(f'Nome atualizado: {npc.nome}')

if __name__ == "__main__":
    main()
