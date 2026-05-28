from personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, maldade, dano, pontos):
        super().__init__(nome, idade, vida)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade
        self.dano = dano
        self.pontos = pontos

    def ataque(self, personagem,pontos):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
       
        personagem.vida -=self.dano*pontos
        if personagem.vida < 0:
            personagem.vida = 0
        print(f'{self.nome} atacou {personagem.nome} com {self.dano *pontos} de dano!')

    def bonificar(self, pontos_bonus):
        self.pontos += pontos_bonus

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
