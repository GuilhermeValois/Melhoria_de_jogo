from personagem import Personagem
from heroi import Heroi
from vilao import Vilao
import random
import emoji
import utils

def main():
    # Criando personagens e vilões
    heroi1 = Heroi('Invencível', 19, 100, 100, 12, 2,2,20)
    heroi2 = Heroi('Eve Atômica', 19, 80, 80, 16, 2,2,10)
    heroi3 = Heroi('Allen', 2000, 130, 130, 10, 3,3,15)
    vilao1 = Vilao('Anissa', 1000, 110, 110, 11, 2,2,11)
    vilao2 = Vilao('Conquista', 5000, 140, 140, 16, 3,3, 16)
    vilao3 = Vilao('Thragg', 5000, 180, 180, 18, 4,4, 25)
    vilaolista = [vilao1, vilao2, vilao3]
    utils.limpar()
    while True:
        heroi_nome = input("Digite o herói que deseja jogar:\n[1]. Invencível\n[2]. Eve Atômica\n[3]. Allen\n")
        if heroi_nome == "1":
            heroi = heroi1
            utils.limpar()
            break
        elif heroi_nome == "2":
            heroi = heroi2
            utils.limpar()
            break
        elif heroi_nome == "3":
            heroi = heroi3
            utils.limpar()
            break
        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 3.")
            continue


    for vilao in vilaolista:
        utils.titulo_História(heroi, vilao)
        heroi.dialogar(vilao)
        utils.limpar()
        utils.titulo_combate()
        utils.status(heroi,vilao)
        while True:
            ataque_heroi = 0
            defesa_heroi = 0
            bonus_heroi = 0

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
        
       

            ataque_vilao = random.randint(0, vilao.pontos)
            resto_pontos = vilao.pontos - ataque_vilao
            defesa_vilao = random.randint(0, resto_pontos)
            bonus_vilao = vilao.pontos - ataque_vilao - defesa_vilao
            
            Ataque_final_heroi = ataque_heroi - defesa_vilao
            Ataque_final_vilao = ataque_vilao - defesa_heroi
        
            if Ataque_final_heroi < 0:
                Ataque_final_heroi = 0
            if Ataque_final_vilao < 0:
                Ataque_final_vilao = 0
            heroi.bonificar(bonus_heroi)
            vilao.bonificar(bonus_vilao)
            
        
            if heroi.Velocidade > vilao.Velocidade: 
                heroi.ataque(vilao, Ataque_final_heroi)
                vilao.ataque(heroi, Ataque_final_vilao)
                if heroi.vida <= 0:
                    print(f"\n{heroi.nome} foi derrotado por {vilao.nome}!")
                    return
                if vilao.vida <= 0:
                    print(f"\n{heroi.nome} derrotou {vilao.nome}!")
                    heroi.vida = heroi.vida_max
                    heroi.pontos = heroi.pontos_max
                    break
        
            elif vilao.Velocidade > heroi.Velocidade:
            
                vilao.ataque(heroi, Ataque_final_vilao)
                heroi.ataque(vilao, Ataque_final_heroi)
                if heroi.vida <= 0:
                    print(f"\n{heroi.nome} foi derrotado por {vilao.nome}!")
                    return
                if vilao.vida <= 0:
                    print(f"\n{heroi.nome} derrotou {vilao.nome}!")
                    heroi.vida = heroi.vida_max
                    heroi.pontos = heroi.pontos_max
                    break
            utils.istribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
            utils.status(heroi,vilao)
       
        
       

 
if __name__ == "__main__":
    main()
