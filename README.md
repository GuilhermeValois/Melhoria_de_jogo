# Viltrumite Showdown

Jogo de combate em terminal desenvolvido em Python utilizando Programação Orientada a Objetos (POO).

## Descrição

O jogo é inspirado no universo de Invincible. O jogador escolhe um herói e enfrenta uma sequência de vilões Viltrumitas em batalhas estratégicas por turnos.

Durante a partida, o jogador deve distribuir seus pontos entre ataque, defesa e bônus para derrotar adversários cada vez mais poderosos.

## Funcionalidades

* Escolha de herói
* Diálogos narrativos entre os personagens
* Evolução de atributos após as batalhas
* Sistema de pontos estratégicos para o combate
* Barras de vida
* Interface aprimorada utilizando a biblioteca Rich
* Histórico de eventos da partida
* Utilização de herança, listas, dicionários e modularização

## Personagens Jogáveis

### Invencível

Personagem equilibrado, com atributos balanceados.

### Allen

Possui maior resistência e capacidade de suportar dano.

### Eve Atômica

Mais ofensiva, porém menos resistente.

## Vilões

### Anissa

Primeira adversária do jogo.

### Conquista

Viltrumita extremamente agressivo e poderoso.

### Thragg

Líder dos Viltrumitas e chefe final do jogo.

## Sistema de Combate

A cada rodada, o jogador distribui seus pontos entre:

* ⚔️ Ataque
* 🛡️ Defesa
* ⭐ Bônus

Os pontos investidos em ataque aumentam o dano causado.

Os pontos investidos em defesa reduzem o dano recebido.

Os pontos investidos em bônus são acumulados para utilização em rodadas futuras.

Além disso, cada personagem possui atributos próprios:

* Vida
* Dano Base
* Velocidade
* Pontos Disponíveis

## Requisitos

* Python 3.10 ou superior
* Biblioteca Rich

Instalação da dependência:

```bash
pip install rich
```

## Como Clonar o Repositório

Clone o projeto utilizando:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd nome-do-repositorio
```

## Como Executar

Execute o arquivo principal:

```bash
python main.py
```

ou

```bash
py main.py
```

## Estrutura do Projeto

```text
├── main.py
├── personagem.py
├── heroi.py
├── vilao.py
├── utils.py
└── README.md
```

## Conceitos Utilizados

* Programação Orientada a Objetos
* Herança
* Encapsulamento
* Listas
* Dicionários
* Estruturas de Repetição
* Estruturas Condicionais
* Modularização de Código

## Autor

Projeto desenvolvido como atividade de Programação Orientada a Objetos.
