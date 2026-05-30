from personagem import Personagem
from heroi import Heroi
from vilao import Vilao
import random
import emoji
import utils

def main():
    # Criando personagens e vilões
    heroi1 = Heroi('Invencível', 100, 100, 12, 2,2,20)
    heroi2 = Heroi('Eve Atômica', 80, 80, 16, 2,2,14)
    heroi3 = Heroi('Allen', 130, 130, 10, 3,3,15)
    vilao1 = Vilao('Anissa', 100, 100, 11, 2,2,11)
    vilao2 = Vilao('Conquista', 140, 140, 16, 3,3, 16)
    vilao3 = Vilao('Thragg', 180, 180, 18, 4,4, 25)
    vilaolista = [vilao1, vilao2, vilao3]
    utils.limpar()
    upgrade_pontos = 0
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
        utils.limpar()
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
            
            ataque_final_heroi = ataque_heroi - defesa_vilao
            ataque_final_vilao = ataque_vilao - defesa_heroi
        
            if ataque_final_heroi < 0:
                ataque_final_heroi = 0
            if ataque_final_vilao < 0:
                ataque_final_vilao = 0

            heroi.bonificar(bonus_heroi)
            vilao.bonificar(bonus_vilao)
            
        
            if heroi.Velocidade > vilao.Velocidade: 
                heroi.ataque(vilao, ataque_final_heroi)
                
                if vilao.vida <= 0:
                    upgrade_pontos += 3
                    utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
                    utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
                    utils.status(heroi,vilao)
                    print(f"\n{heroi.nome} derrotou {vilao.nome}!")
                    input("Pressione Enter para continuar...")
                    utils.menu_de_melhora(heroi,upgrade_pontos)
                    heroi.vida = heroi.vida_max
                    heroi.pontos = heroi.pontos_base
                    break
                vilao.ataque(heroi, ataque_final_vilao)
                if heroi.vida <= 0:
                    utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
                    utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
                    utils.status(heroi,vilao)
                    print(f"\n{heroi.nome} foi derrotado por {vilao.nome}!FIM DE JOGO!")
                    return
                
        
            elif vilao.Velocidade > heroi.Velocidade:
            
                vilao.ataque(heroi, ataque_final_vilao)
                
                if heroi.vida <= 0:
                    utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
                    utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
                    utils.status(heroi,vilao)
                    print(f"\n{heroi.nome} foi derrotado por {vilao.nome}!")
                    return
                heroi.ataque(vilao, ataque_final_heroi)
                if vilao.vida <= 0:
                    upgrade_pontos += 3
                    utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
                    utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
                    utils.status(heroi,vilao)
                    print(f"\n{heroi.nome} derrotou {vilao.nome}!")
                    input("Pressione Enter para continuar...")
                    utils.menu_de_melhora(heroi,upgrade_pontos)
                    heroi.vida = heroi.vida_max
                    heroi.pontos = heroi.pontos_max
                    break
            
            utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
            utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
            utils.status(heroi,vilao)
       
        
       

 
if __name__ == "__main__":
    main()
