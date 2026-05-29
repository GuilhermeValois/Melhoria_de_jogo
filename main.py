from personagem import Personagem
from heroi import Heroi
from vilao import Vilao
import random
import emoji
import rich
import utils

def main():
    # Criando personagens e vilões
    vilao1 = Vilao('Anissa', 3000, 100, 100, 20, 2)
    vilao2 = Vilao('Conquista', 5000, 120, 120, 25, 2)
    vilao3 = Vilao('Thragg', 4000, 180, 180, 25, 30)
    while True:
        heroi_nome = input("Digite o nome do herói: ")
        if heroi_nome:
            heroi = Heroi(heroi_nome, 19, 100, 100, 12, 2)
            utils.limpar()
            break

    
    
    heroi.dialogar(vilao2)
    utils.limpar()
    utils.titulo_combate()
    utils.status(heroi)
    utils.status(vilao2)
    while True:
        ataque_heroi = 0
        defesa_heroi = 0
        bonus_heroi = 0

        if heroi.vida <= 0:
            print(f"\n{heroi.nome} foi derrotado por {vilao2.nome}!")
            break
        if vilao2.vida <= 0:
            print(f"\n{vilao2.nome} foi derrotado por {heroi.nome}!")
            break

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
        
       

        ataque_vilao = random.randint(0, vilao2.pontos)
        resto_pontos = vilao2.pontos - ataque_vilao
        defesa_vilao = random.randint(0, resto_pontos)
        bonus_vilao = vilao2.pontos - ataque_vilao - defesa_vilao
        

        

        Ataque_final_heroi = ataque_heroi - defesa_vilao
        Ataque_final_vilao = ataque_vilao - defesa_heroi
        if Ataque_final_heroi < 0:
            Ataque_final_heroi = 0
        if Ataque_final_vilao < 0:
            Ataque_final_vilao = 0

        heroi.pontos = 2 + bonus_heroi
        vilao2.pontos = 2 + bonus_vilao
       
        heroi.ataque(vilao2, Ataque_final_heroi)
        
        vilao2.ataque(heroi, Ataque_final_vilao)
        
        utils.status(heroi)
        utils.status(vilao2)
        
       

 
if __name__ == "__main__":
    main()
