import pygame, random
from pygame.locals import *

#função para gerar a posição da maçã nas posições corretas do grid
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x // 10 * 10, y // 10 * 10)

#função para detectar a colisão entre a cobra e a maça
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#Direções da cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Criando o display(tela) do jogo
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

#Criando a cobra com seu tamanho inicial
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

#Gerando a maçã em uma posiçao aleatória no grid
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255, 0, 0))

#direção inicial da cobra
my_direction = LEFT

#variável para definir a velocidade da cobra
clock = pygame.time.Clock()

#Laço infinito para que o jogo fique sempre rodando
score = 0
game_over = False
while not game_over:
    #velocidade da cobra
    clock.tick(20)

    #loop para pegar os eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #Direcionamento da cobra
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    #Detectando colisão com a maçã
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    #movimentação da cobra
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    #definindo o redirecionamento da cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    #detectando colisão com as bordas
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    #detectando se a cobra colidio consigo mesma
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    score_font = pygame.font.Font('freesansbold.ttf', 32)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_score_screen = score_font.render('Score: ' + str(score), True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    score_rect = game_over_score_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    score_rect.midtop = (600 / 2, 100)
    screen.blit(game_over_screen, game_over_rect)
    screen.blit(game_over_score_screen, score_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()