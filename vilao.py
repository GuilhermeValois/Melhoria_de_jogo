from personagem import Personagem 
import random # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida,vida_max, dano, pontos,pontos_base,velocidade):
        super().__init__(nome, vida)
        self.vida_max = vida_max
        self.dano = dano
        self.pontos = pontos
        self.pontos_base = pontos_base
        self.Velocidade = velocidade

    def ataque(self, personagem,pontos): 
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        personagem.vida -=self.dano*pontos
        if personagem.vida < 0:
            personagem.vida = 0
        

    def bonificar(self, pontos_bonus):
        
        self.pontos = self.pontos_base + pontos_bonus
        
        if self.pontos > 8:
            self.pontos = 8

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Dano: {self.dano}, Pontos: {self.pontos}'
