o jogo foi feito em python usando pygame

o que é pygame?

Pygame é uma biblioteca de jogos multiplataforma (independente de sistema operacional) feita para ser utilizada em conjunto com a linguagem de programação Python. O seu nome tem origem da junção de Py, proveniente de Python e Game, que significa Jogo, ou seja, Jogos em Python.

Pygame se baseia na ideia de que as tarefas mais intensivas computacionalmente em um jogo podem ser abstraídas separadamente da lógica principal, ou seja, o uso de memória e CPU (úteis para processar imagens e sons) são tratados pelo próprio código do Pygame e não pelo código do seu jogo. Assim, possibilita-se utilizar uma linguagem de alto nível, como Perl, Lua ou Python para organizar a estrutura do jogo em si.

História
O desenvolvimento da biblioteca Pygame começou no ano 2000 por Pete Shinners que, familiarizado com a linguagem de programação C, descobriu a linguagem Python e a biblioteca SDL (Simple Directmedia Library) ao mesmo tempo.

A SDL é uma biblioteca escrita em linguagem C que controla os recursos de multimídia e é utilizada por várias aplicações de código-aberto e por aplicações comerciais empresariais.

A descontinuidade da implementação da SDL em Python por Mark Baker denominada PySDL inspirou-o a começar um projeto robusto, também em Python, sob a SDL, chamada Pygame.[1]

Sua intenção era

“	Fazer as coisas simples de maneira fácil e as coisas difíceis de maneira direta.	”
O que é Python
 Ver artigo principal: Python
Python é uma linguagem de alto-nível interpretada, interativa, orientada a objetos, de tipagem dinâmica e forte.

A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.

Pete Shinners, quando começou a desenvolver o Pygame, afirmou, sobre o modo como Python facilita a programação, que "queria um projeto que realmente tirasse proveito de Python" e queria que os módulos do Pygame também explicitassem essa clareza e simplicidade.[1]

O que é SDL
 Ver artigo principal: SDL
Simple DirectMedia Layer (SDL) é uma biblioteca multimídia e multiplataforma escrita em C, possui interfaces para outras linguagens de programação, como Ada, Eiffel, Java, Lua, ML, Perl, PHP, Ruby e também para Python, que cria uma abstração em várias plataformas de gráficos, sons, e entrada de APIs, possibilitando ao programador escrever um jogo de computador ou outra aplicação multimedia já que pode rodar em vários tipos de sistema operacionais. Gerencia video, eventos, audio digital, CD-ROM, som, threads, processamento de objetos compartilhados, rede e tempo.

Pygame é um jogo?
Pygame é um "motor de jogo" ou em inglês "game engine". Um motor de jogo é um software ou um conjunto de bibliotecas usado na simplificação do desenvolvimento de jogos, por exemplo, para videogames e computadores.

As funcionalidades típicas fornecidas por um motor de jogo incluem o mecanismo de renderização (ou rendering engine) para gráficos 2D ou 3D, um mecanismo de detecção de colisão, suporte a sons, uma linguagem de script, suporte à animação, inteligência artificial e jogos pela internet.

Ou seja, é utilizado um motor de jogo que contém todas as funções visuais e de processamento como base do código, e a essência do jogo como a estratégia, o design e a ideia principal que serão realmente pensadas e estudadas para o jogo.

Eventos essenciais
Abaixo, apresentam-se alguns dos eventos mais importantes na concepção de um jogo, como cores, superfície, manipulação da tela ou sons.

Surface são as superfícies em 2D ou 3D onde se desenha o jogo, podendo preencher uma área com uma cor ou mudar a cor da superfície dependendo da posição, e outros recursos como transparência.
Display é o eventos para manipulação da tela do jogo, podendo atualizar o conteúdo da tela, retornar a superfície que representa a tela ou configurar o tamanho da tela.
draw são os desenhos na superfície, em linha, círculo, retângulo ou polígono.
image são as imagens, podendo ler ou gravar as imagens.
event são os eventos de um jogo, algumas operações como o poll() retorna o próximo evento da fila de eventos ou post() que coloca um evento na fila.
font é utilizado para trabalhar com fontes TrueType, podendo utilizar o render() para retornar uma superfície com o teto desenhado ou size() que calcula o tamanho da superfície que irá escrever nela.
transform pode rotacionar, espelhar, modificar ou cortar as superfícies do jogo.
mixer trabalha com os sons do jogo.
Clock trabalha com o tempo dos quadros do jogo.
sprite é uma imagem bi-dimensional que faz parte de uma cena maior, isto é, os componentes que aparecem no jogo. Podendo se dividir em Sprite e Group, a classe Group serve para agrupar vários Sprites.
Detectando colisões durante um jogo
A detecção de colisão é um dos recursos mais utilizados em jogos. A colisão entre objetos de um jogo acontece porque dentro do jogo não há formas físicas, logo, se o código do jogo não prevê quando um objeto se sobrepõe a outro, o jogo terá, certamente, defeitos.

Exemplificando: se no jogo Super Mario não estivesse prevista a colisão do "Mario" com a parede, o Mario iria passar por dentro da parede e o jogo estaria com um sério problema de colisão. Como a colisão é tratada, o Mario não pode ultrapassar os limites exteriores da parede, tendo obrigatoriamente de pular ou passar por cima dela.

A implementação de colisões pode ser dada de várias formas, o Projeto de um Jogo de Tiro ao Alvo 3D[2] explica que uma das formas de tratar a colisão recorre à técnica de volumes envoltórios de esféricos. Todo objeto de um "Sprite" ou de um "Group" será associado a um esfera com centro no centróide do objeto e com raio igual à distância entre o centróide do objeto e o ponto do objeto mais distante do centróide, com um fator de escala aplicado para reduzir um pouco esse raio, para que o volume não seja muito maior que o objeto, caso este apresente uma dimensão bem maior que as outras.

Desta forma, para verificar uma colisão basta saber se a distância entre os centróides de dois objetos é maior que a soma dos raios de suas respectivas esferas envoltórias, se a distância é menor, os dois objetos colidiriam.

No Pygame existem dois recursos para o tratamento de colisões: um é o "spritecollide" que detecta a colisão do "Sprite" com os elementos do grupo, e o "groupcollide" que detecta a colisão dos "Sprites" de cada "Group" do jogo.

Visão geral do código
Pygame é escrito em Linguagem C e Python, necessitando de recursos da SDL como o SDL 1.2.6, SDL_image 1.2.3, SDL_ttf 2.0.6, SDL_mixer 1.2.5 e SMPEG 0.4.4 e Numeric 23.0.[3]

Abaixo, apresenta-se um resumo sobre os módulos que o Pygame contém para o desenvolvimento de jogos.[1]

cdrom: gerencia o dispositivo de cdrom e a execução do áudio.
cursors: carrega imagens de cursores como mouse.
display: controle a exibição da tela ou janela.
draw: desenha formas simples sobre uma superfície.
event: controla eventos e a fila de eventos.
font: cria e renderiza fontes Truetype.
image: grava e carrega imagens.
joystick: controla dispositivos de joystick.
key: controla o teclado.
mouse: controla o mouse.
movie: executa filmes no formato mpeg.
sndarray: manipula sons com Numeric.
surfarray: manipula imagens com Numeric.
time: controla o tempo dos eventos.
transform: escalar, rotacionar e girar imagens.
Exemplos de códigos
Abaixo um código de exemplo obtido do site oficial do pygame,[1] faz uma animação de uma bola saltando.

import sys, pygame

pygame.init()
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)  # define o tamanho da tela
ball = pygame.image.load("ball.bmp")    # carrega a imagem da bola
ballrect = ball.get_rect()
while 1:                                # cria um loop infinito
    for event in pygame.event.get():    # se houver algum evento do usuário,
        if event.type == pygame.QUIT:   # o programa termina
           sys.exit()

# movimentação da bola e atualização da tela
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
       speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
       speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
Outros exemplos de códigos:

Exemplo de um cubo em três dimensões
Livro de receitas de códigos do site oficial do Pygame
Lentidão do Python
Um dos grandes problemas do Python é sua lentidão no processamento de imagens e iterações..[4] Depois de descobrir onde está a lentidão do programa com recursos próprios da linguagem Python como "timeit", "profile" ou hotshot", uma das soluções mais utilizadas é escrever uma extensão em linguagem C do código lento do seu programa em Python.

Outra solução para otimizar sua aplicação é o uso de um compilador JIT para o Python, como por exemplo, o programa "Psyco" que gera um ganho de 4 vezes mais velocidade mas utiliza muita memória do computador.[5]

Ver também
Cocos2d
Panda3D
Referências
 «Python Pygame Introduction» (em inglês). Consultado em 11 de setembro de 2010. Arquivado do original em 15 de agosto de 2011
Descrição do Projeto de um Jogo de Tiro ao Alvo 3D em Português
Repositório do projeto Pygame no Seul.org
Apresentação de Gustavo Barbieri sobre Pygame em Português
Apresentação de Rudá Moura sobre "Porque Python é tão lento?" em Português
Ligações externas
«Página oficial» (em inglês)
[Esconder]vde
Motores de jogo e middleware
Desenvolvimento de jogos eletrônicos · Motor gráfico · Motor de física · Sistema de criação de jogos · Source port
BulletCocos2dCryEngineFrostbiteGamebryoGameMakerGodotHavokid TechIrrlichtjMonkeyEnginelibGDXMonoGameODEOGREPanda3DPhysXPygameraylibRenderWareRPG MakerSDLSourceThree.jsTorqueUnityUnreal Enginemais...
Página de categoria Categoria · Lista Lista
Categorias: Motores de jogoSoftware livreBibliotecas PythonSoftware livre programado em PythonSoftware de desenvolvimento de jogos eletrônicosSoftware de desenvolvimento de jogos eletrônicos para LinuxAPIs do LinuxAPIs do WindowsAPIs do macOS
