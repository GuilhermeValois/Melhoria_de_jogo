from personagem import Personagem  # Importa a classe Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome,vida,vida_max, dano, pontos,pontos_base,velocidade):
        super().__init__(nome, vida)
        self.vida_max = vida_max
        self.dano = dano
        self.pontos = pontos
        self.pontos_base = pontos_base
        self.velocidade = velocidade

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
    
    def melhorar(self, opção):
        if opção == "1":
            self.upgrade_vida()
        elif opção == "2":
            self.upgrade_dano()
        elif opção == "3":
            self.upgrade_velocidade()
        elif opção == "4":
            self.upgrade_pontos_base()

    def __str__(self):
        return f'Herói: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'