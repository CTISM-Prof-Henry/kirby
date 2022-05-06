import pygame
from pygame.locals import *

from entities import Player

from game_rules import *
from screen import Screen


def check_events(my_direction: int):
    """
    Verifica eventos do jogo (incluindo se teclas foram pressionadas)

    :param my_direction: A direção do jogador
    :return: A nova direção do jogador, atualizada com base nas teclas pressionadas neste instante
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DIR_DOWN:
                my_direction = DIR_UP
            if event.key == K_DOWN and my_direction != DIR_UP:
                my_direction = DIR_DOWN
            if event.key == K_LEFT and my_direction != DIR_RIGHT:
                my_direction = DIR_LEFT
            if event.key == K_RIGHT and my_direction != DIR_LEFT:
                my_direction = DIR_RIGHT
            if event.key == K_ESCAPE:
                exit(0)
        else:
            my_direction = None

    return my_direction


def check_collisions(entities, score: int, game_over: bool, victory: bool):
    """
    Verifica colisões de entidades no jogo.
    """
    pass


def main():
    pygame.init()
    pygame.display.set_caption('Kirby')
    clock = pygame.time.Clock()
    screen = Screen(screen_width, screen_height, grid_size)

    player = Player(0, 0, collision_box=None)
    my_direction = None

    entities = [player]

    score = 0
    game_over = False
    victory = False
    while not game_over:
        clock.tick(10)
        my_direction = check_events(my_direction)

        if victory:
            break

        if game_over:
            break

        player.move(my_direction)
        screen.render(entities, score=score)
        pygame.display.update()

    if game_over:
        screen.show_screen(width=screen_width, message='Game Over')
    elif victory:
        screen.show_screen(width=screen_width, message='Você ganhou!')


if __name__ == '__main__':
    main()
