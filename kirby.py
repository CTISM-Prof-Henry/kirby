import pygame
import numpy as np
from pygame.locals import *

# direções do aspirador
from entities import Player, Entity

from game_rules import *
from screen import Screen


def check_events(my_direction: int):
    """
    Verifica eventos do jogo (incluindo se teclas foram pressionadas)

    :param my_direction: A direção do aspirador
    :return: A nova direção do aspirador, atualizada com base nas teclas pressionadas neste instante
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
    pygame.display.set_caption('Pitfall')
    clock = pygame.time.Clock()
    screen = Screen(screen_width, screen_height, grid_size)

    player = Player(0, 0, collision_box=None)
    my_direction = None
    # dirts = generate_random_positions(screen_width, screen_height, how_dirty=n_dirt)

    entities = [player]

    score = 0
    game_over = False
    victory = False
    while not game_over:
        clock.tick(10)
        my_direction = check_events(my_direction)

        # player, dirts, score, game_over, victory = check_collisions(player, dirts, score, game_over, victory)
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
