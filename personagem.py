from rich.console import Console
class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida_max += incremento
        print(f'{self.nome} recebeu {incremento} de vida. Vida atual: {self.vida_max}')
        input("Pressione Enter para continuar...")


    def upgrade_dano(self, incremento=1):
        """
        Aumenta o dano do personagem. O valor padrão de incremento é 1.
        """
        self.dano += incremento
        print(f'{self.nome} recebeu {incremento} de dano. Dano atual: {self.dano}')
        input("Pressione Enter para continuar...")

    def upgrade_velocidade(self, incremento=4):
        """
        Aumenta a velocidade do personagem. O valor padrão de incremento é 1.
        """
        self.velocidade += incremento
        print(f'{self.nome} recebeu {incremento} de velocidade. Velocidade atual: {self.velocidade}')
        input("Pressione Enter para continuar...")

    def upgrade_pontos_base(self, incremento=1):
        """
        Aumenta os pontos base do personagem. O valor padrão de incremento é 1.
        """
        if self.nome == "Eve Atômica" or self.nome == "Invencível":
            if self.pontos_base < 3:
                self.pontos_base += incremento
                print(f'{self.nome} recebeu {incremento} de pontos base. Pontos base atuais: {self.pontos_base}')
            else:
                print(f'{self.nome} já atingiu o limite de pontos base. Pontos base atual: {self.pontos_base}')
        if self.nome == "Allen":
            if self.pontos_base < 4:
                self.pontos_base += incremento
                print(f'{self.nome} recebeu {incremento} de pontos base. Pontos base atuais: {self.pontos_base}')
            else:
                print(f'{self.nome} já atingiu o limite de pontos base. Pontos base atual: {self.pontos_base}')
        input("Pressione Enter para continuar...")
        

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
            "🟣 Anissa: Não está claro?\n"
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
            "Uma silhueta enorme surge acima dele, o cobrindo completamente com sua sombra.\n",
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

            console.print(
            f"\nAnos se passaram desde a batalha contra Conquista.\n"
            f"{self.nome} entende que para por fim em tudo, presica derrotar Thragg.\n"
            f"Então junto da Coalizão de Planetas parte rumo Guerra Viltrmita.\n",
            style="white"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"Então {self.nome} se depara com o grande regente do Império Viltrumita.\n",
            style="white"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "👑 Thragg: Então é você.\n",
            style="bold yellow"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: ...\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "👑 Thragg: O responsável pela resistência terrestre.\n"
            "O responsável por desafiar o Império repetidas vezes.\n",
            style="bold yellow"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: Você é Thragg.\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "👑 Thragg: Vejo que meu nome ainda inspira respeito.\n",
            style="bold yellow"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: Respeito não é a palavra que eu usaria.\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "👑 Thragg: Anissa falhou.\n"
            "Conquista falhou.\n"
            "E agora o Império perdeu a paciência.\n",
            style="bold yellow"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: Então veio terminar o trabalho?\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "👑 Thragg: Não.\n",
            style="bold yellow"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "👑 Thragg: Eu vim provar por que sou o regente dos Viltrumitas.\n",
            style="bold yellow"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            f"🔵 {self.nome}: EU MATEI O CONQUISTA!.\n",
            style="bold cyan"
            )

            input("Pressione Enter para continuar...\n")

            console.print(
            "👑 Thragg: Conquista não passava de um cachorrinho meu.\n",
            style="bold yellow"
            )

            input("Pressione Enter para iniciar combate...\n")


            

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
