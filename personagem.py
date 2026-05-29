from rich.console import Console
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
            
            console = Console()

            console.print(
            f"\nO dia estava tranquilo. {self.nome} patrulhava pelas ruas "
            "fazendo a segurança da cidade.\n"
            "Uma figura pousa lentamente atrás dele.\n",
            style="white"
            )

            input("\nPressione Enter para continuar...\n")

            console.print(
            "🟣 Anissa: Olhe ao seu redor...\n"
            " Anissa: Você ainda insiste em proteger este planeta?\n",
            style="bold magenta"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: Eu já disse que a Terra não pertence aos Viltrumitas.\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "🟣 Anissa: Olhe ao seu redor...\n"
            "Guerras... Fome... Doenças...\n"
            "Nós poderíamos acabar com tudo isso em poucos anos.\n",
            style="bold magenta"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: Não à custa da liberdade da humanidade.\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
                "🟣 Anissa: Lembre-se de que tentamos conversar.\n",
                style="bold magenta"
                )

            input("Pressione Enter para iniciar combate...\n")

        if personagem.nome == "Conquista":

            console = Console()
            
            console.print(
            "🟣 Anissa: Alguém pior do que eu virá...\n",
            style="bold magenta"
            )

            console.print(
            f"\nApós o combate contra Anissa, meses se passaram.\n"

            f"{self.nome} se encontra aflito entre os escombros "
            "dos eventos após a Guerra Invencível.\n"
            "Uma silhueta enorme surge acima dele, cobrindo tudo com sua sombra.\n",
            style="white"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "🔴 Conquista: Esteja pronto para minha chegada, verme.\n",
            style="bold red"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "🔴 Conquista: Você recebeu ordens.\n"
            "Você recebeu tempo.\n"
            "Recebeu mais tolerância do que a maioria.\n",
            style="bold red"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "🔴 Conquista: E mesmo assim, encontrei este planeta "
            "despreparado para a chegada do Império Viltrumita.\n",
            style="bold red"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: Argh... Não é um bom momento.\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "🔴 Conquista: O Império previu sua resistência.\n"
            "Foi por isso que me enviaram.\n",
            style="bold red"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
             "🔴 Conquista: Eu sou Conquista!\n"
            "Sua última chance de cumprir seu dever!\n",
            style="bold red"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: Você não entende...\n"
            "Toda essa destruição é culpa minha.\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: Tudo o que eu quero fazer agora é...\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: BATER EM ALGO O MAIS FORTE QUE EU PUDER!!!\n",
            style="bold bright_cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "🔴 Conquista: Ótimo.\n",
            style="bold red"
            )

            input("Pressione Enter para iniciar combate...\n")

        if personagem == "Thragg":

            print(f"""'Após o combate contra Conquista, meses se passaram. {self.nome} se encontra aflito nos escombros após os eventos da Guerra Invencível. Quando uma silhueta enorme aparece fazendo sobre ele.\n""")

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
