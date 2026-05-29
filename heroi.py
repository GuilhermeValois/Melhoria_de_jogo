from personagem import Personagem  # Importa a classe Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida,vida_max, dano, pontos,pontos_base,Velocidade):
        super().__init__(nome, idade, vida)
        self.vida_max = vida_max
        self.dano = dano
        self.pontos = pontos
        self.pontos_base = pontos_base
        self.Velocidade = Velocidade

    def ataque(self, personagem,pontos):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        personagem.vida -=self.dano*pontos
        if personagem.vida < 0:
            personagem.vida = 0

        
    
    def bonificar(self, pontos_bonus):
        if self.pontos < 4:
            self.pontos = self.pontos_base + pontos_bonus + 1
        elif self.pontos >= 4 and self.pontos < 8:
            self.pontos = self.pontos_base + pontos_bonus
        else:
            self.pontos = 8


    def __str__(self):
        return f'Herói: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'