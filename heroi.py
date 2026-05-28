from personagem import Personagem  # Importa a classe Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, dano, pontos):
        super().__init__(nome, idade, vida)
        self.dano = dano
        self.pontos = pontos

    def ataque(self, personagem,pontos):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        personagem.vida -=self.dano*pontos
        if personagem.vida < 0:
            personagem.vida = 0
        print(f'{self.nome} atacou {personagem.nome} com {self.dano * pontos} de dano!')
        
    
    def bonificar(self, pontos_bonus):
        2 + pontos_bonus

    def __str__(self):
        return f'Herói: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'