# Kirby

Este repositório visa ensinar a programação de jogos utilizando a biblioteca [Pygame](https://www.pygame.org/news) e o 
jogo [Kirby's Adventure](https://en.wikipedia.org/wiki/Kirby%27s_Adventure), para NES.

<img src="images/walking.gif" width="100px">

## Sumário

1. [Instruções](#instruções)
2. [Exercícios](#exercícios)
3. [Referências](#referências)

## Instruções

### Instalação (para Windows)

**Nota:** não é preciso fazer esse passo nos computadores da escola.

1. Baixe o Visual Studio Community na sua máquina, através 
deste [link](https://visualstudio.microsoft.com/pt-br/downloads/)
2. No instalador, marque a opção de **Ferramentas de Desenvolvimento para C++**

### Instalação (para Linux)

**Nota:** não é preciso fazer esse passo nos computadores da escola.

1. Instale o GNU C Compiler (gcc):

```bash
sudo apt install gcc --assume-yes
```

### Configuração (para Windows)

1. Abra o [prompt de comando do Python Anaconda](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/anaconda.md#e-o-que-fazer-se-fiz-errado)

2. Se você ainda não fez isso, crie um novo ambiente virtual:

```bash
conda create --name ctism pip --yes
```

3. Ative-o:

```bash
conda activate ctism
```

4. Instale as dependências do `pip` (faça isso mesmo se você já tiver um ambiente virtual configurado):

````bash
pip install --requirement requirements.txt --yes
````

### Rodando o código pela linha de comando

```bash
python kirby.py
```

### Rodando o código pelo Pycharm

Confira os tutoriais do pythonEssentials, se for a 
[primeira vez](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/pycharm.md#primeira-configura%C3%A7%C3%A3o) que estiver configurando, ou se forem 
[configurações subsequentes](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/pycharm.md#configura%C3%A7%C3%B5es-subsequentes)

## Exercícios

1. Faça o Kirby piscar os olhos **(resolvido)**  
2. Faça o Kirby andar (ou em outras palavras, troque os sprites quando ele anda).
3. Faça o jogo ter um chão. Faça o Kirby "nascer" no chão, e cair com a gravidade quando pular.
4. Coloque alguns inimigos no jogo.
5. Faça o Kirby atacar os inimigos, e faça que eles morram quando forem atacados (_one hit kill_).

## Referências

* [Página inicial da biblioteca pygame](https://www.pygame.org/news)
* [Documentação pygame](https://www.pygame.org/docs/)
* [Sprites do Jogo Kirby's Adventure](https://spritedatabase.net/game/228)
* [Gameplay de Kirby's Adventure](https://www.youtube.com/watch?v=LyU-mKTAauk)