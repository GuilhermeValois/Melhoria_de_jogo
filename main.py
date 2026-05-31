from personagem import Personagem
from heroi import Heroi
from vilao import Vilao
import random
import json
import utils

def main():

    
    # Criando personagens e vilões
    heroi1 = Heroi('Invencível', 100, 100, 12, 2,2,20)
    heroi2 = Heroi('Eve Atômica', 80, 80, 16, 2,2,14)
    heroi3 = Heroi('Allen', 130, 130, 10, 3,3,15)
    vilao1 = Vilao('Anissa', 100, 100, 11, 2,2,11)
    vilao2 = Vilao('Conquista', 140, 140, 16, 3,3, 16)
    vilao3 = Vilao('Thragg', 180, 180, 18, 4,4, 25)
    historico_jogo = []
    historico_batalha = []
    vilao_lista = [vilao1, vilao2, vilao3]
    
    personagens_lista = [heroi1, heroi2, heroi3, vilao1, vilao2, vilao3]
    personagens_dicionarios = []
    
    for personagem in personagens_lista:
        personagem_descricao = {
            'nome': personagem.nome,
            'vida': personagem.vida,
            'vida máxima': personagem.vida_max,
            'dano': personagem.dano,
            'pontos': personagem.pontos,
            'pontos base': personagem.pontos_base,
            'velocidade': personagem.velocidade
        }
        personagens_dicionarios.append(personagem_descricao)
    utils.salvar_personagens(personagens_dicionarios)
    
    

    utils.limpar()
    upgrade_pontos = 0
    while True:

        utils.escolher_heroi(heroi1, heroi2, heroi3)
        heroi_nome = input()
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
            utils.limpar()
            print("Opção inválida! Por favor, escolha um número entre 1 e 3.")
            
            continue


    for vilao in vilao_lista:
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
            
        
            if heroi.velocidade > vilao.velocidade: 
                heroi.ataque(vilao, ataque_final_heroi)
                
                if vilao.vida <= 0:
                    upgrade_pontos += 3
                    utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
                    utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
                    historico_batalha.append(f"{heroi.nome} atacou com {ataque_final_heroi*heroi.dano} de dano\nVITÓRIA")
                    registro = {'vilão': vilao.nome,'histórico': historico_batalha}
                    historico_jogo.append(registro)
                    utils.salvar_historico(historico_jogo)
                    utils.status(heroi,vilao)
                    utils.vitoria(vilao)
                    input("Pressione Enter para continuar...")
                    utils.menu_de_melhora(heroi,upgrade_pontos)
                    heroi.vida = heroi.vida_max
                    heroi.pontos = heroi.pontos_base
                    break
                vilao.ataque(heroi, ataque_final_vilao)
                if heroi.vida <= 0:
                    utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
                    utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
                    historico_batalha.append(f"{heroi.nome} atacou com {ataque_final_heroi*heroi.dano} de dano e {vilao.nome} atacou com {ataque_final_vilao*vilao.dano} de dano\nDERRTOA ")
                    registro = {'vilão': vilao.nome,'histórico': historico_batalha}
                    historico_jogo.append(registro)
                    utils.salvar_historico(historico_jogo)
                    utils.status(heroi,vilao)
                    utils.derrota(vilao)
                    input("Pressione Enter para continuar...")
                    return
                
        
            elif vilao.velocidade > heroi.velocidade:
            
                vilao.ataque(heroi, ataque_final_vilao)
                
                if heroi.vida <= 0:
                    utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
                    utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
                    historico_batalha.append(f"{vilao.nome} atacou com {ataque_final_vilao*vilao.dano} de dano\nDERRTOA ")
                    registro = {'vilão': vilao.nome,'histórico': historico_batalha}
                    historico_jogo.append(registro)
                    utils.salvar_historico(historico_jogo)
                    utils.status(heroi,vilao)
                    utils.derrota(vilao)
                    input("Pressione Enter para continuar...")
                    return
                heroi.ataque(vilao, ataque_final_heroi)
                if vilao.vida <= 0:
                    upgrade_pontos += 3
                    utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
                    utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
                    historico_batalha.append(f"{vilao.nome} atacou com {ataque_final_vilao*vilao.dano} de dano e {heroi.nome} atacou com {ataque_final_heroi*heroi.dano} de dano\nVITÓRIA") 
                    registro = {'vilão': vilao.nome,'histórico': historico_batalha}
                    historico_jogo.append(registro)
                    utils.salvar_historico(historico_jogo)
                    utils.status(heroi,vilao)
                    utils.vitoria(vilao)
                    input("Pressione Enter para continuar...")
                    utils.menu_de_melhora(heroi,upgrade_pontos)
                    heroi.vida = heroi.vida_max
                    heroi.pontos = heroi.pontos_base
                    break
            
            utils.distribuição_pontos(heroi, ataque_heroi, defesa_heroi, bonus_heroi, vilao, ataque_vilao, defesa_vilao, bonus_vilao)
            utils.resultado(heroi,vilao,ataque_final_heroi,ataque_final_vilao)
            if heroi.velocidade > vilao.velocidade:
                historico_batalha.append(f"{heroi.nome} atacou com {ataque_final_heroi} de dano e {vilao.nome} atacou com {ataque_final_vilao} de dano\n")
            else:
                historico_batalha.append(f"{vilao.nome} atacou com {ataque_final_vilao} de dano e {heroi.nome} atacou com {ataque_final_heroi} de dano\n")
            utils.status(heroi,vilao)
       
        
       

 
if __name__ == "__main__":
    main()
