import rich

class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida):
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')


    def downgrade_vida(self):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > 15:
            self.vida -= 15
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def dialogar(self, personagem):

        if personagem.nome == "Anissa":
            print(f"""'O dia estava tranquilo. {self.nome} patrulhava pelas ruas fazendo a\nsegurança da cidade Quando ma figura pousa lentamente atrás dele.'\n""")
            
            input("Pressione Enter para continuar...\n")
            
            print('Anissa: Você ainda insiste em proteger este planeta?\n')

            input("Pressione Enter para continuar...\n")

            print(f'{self.nome}: Eu já disse que a Terra não pertence aos Viltrumitas.\n')

            input("Pressione Enter para continuar...\n")

            print(f"""Anissa: Olhe ao seu redor, Guerras...Fome...Doenças...\nNós poderíamos acabar com tudo isso em poucos anos.\n""")

            input("Pressione Enter para continuar...\n")

            print(f'{self.nome}: Não à custa da liberdade da humanidade.\n')

            input("Pressione Enter para continuar...\n")

            print('Anissa:Lembre-se de que tentamos conversar.\n')

            input("Pressione Enter para iniciar combate\n")

        if personagem.nome == "Conquista":
            
            print('Anissa: Alguém pior do que eu Virá...\n')

            print(f"""Após o combate contra Anissa, meses se passaram. {self.nome} se encontra aflito nos escombros\ndos eventos após a Guerra Invencível. Quando uma silhueta enorme aparece fazendo sombra sobre ele.\n""")
            
            input("Pressione Enter para continuar...\n")
            
            print('Conquista: Esteja pronto para minha chegada, Verme.\n')

            input("Pressione Enter para continuar...\n")

            print(f"""Conquista: Você recebeu ordens. Você recebeu tempo. Recebeu mais Tolerância do que a maioria\n""")

            input("Pressione Enter para continuar...\n")

            print("""Conquista: E mesmo assim, encontrei este planeta despreparado para a chegada do nosso império viltrum\n""")

            input("Pressione Enter para continuar...\n")

            print(f'{self.nome}: Argh... Não é um bom mommento.\n')

            input("Pressione Enter para continuar...\n")

            print('Conquista: O império previu sua resistência e foi por isso que me enviaram.\n')

            input("Pressione Enter para continuar...\n")

            print('Conquista: Eu sou a Conquista! Eu sou a última chance de você cumprir o seu dever!\n')

            input("Pressione Enter para continuar...\n")

            print(f'{self.nome}: Você não entende. Toda essa destruição é culpa minha.\n')

            input("Pressione Enter para continuar...\n")

            print(f'{self.nome}: Tudo que eu quero fazer agora é...\n')

            input("Pressione Enter para continuar...\n")

            print(f'{self.nome}: Bater em algo O MAIS FORTE QUE EU PUDER!!!\n')

            input("Pressione Enter para continuar...\n")

            print('Conquista: Ótimo\n')


            input("Pressione Enter para iniciar combate")

        if personagem == "Thragg":

            print(f"""'Após o combate contra Conquista, meses se passaram. {self.nome} se encontra aflito nos escombros após os eventos da Guerra Invencível. Quando uma silhueta enorme aparece fazendo sobre ele.\n""")

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
