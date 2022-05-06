import pygame
from pygame.constants import QUIT, K_ESCAPE


class Screen(object):
    def __init__(self, width, height, grid_size):
        self.height = height
        self.width = width
        self.grid_size = grid_size

        self.screen = pygame.display.set_mode((width, height))

        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.score_font = self.font.render('Score: %s' % 0, True, (255, 255, 255))
        self.score_rect = self.score_font.get_rect()
        self.score_rect.topleft = (self.width - 120, grid_size)

    def draw_grid(self):
        """
        Desenha o grid na tela do jogo

        :param height: Altura da janela
        :param width: Largura da janela
        """

        for x in range(0, self.width, self.grid_size):  # Draw vertical lines
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, self.width))
        for y in range(0, self.height, self.grid_size):  # Draw vertical lines
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (self.height, y))

    def render(self, entities, score):
        self.screen.fill((0, 0, 0))  # pinta a tela de preto

        # dirt_skin = pygame.Surface((grid_size, grid_size))
        # dirt_skin.fill((139, 69, 19))  # a sujeira é marrom
        # for dirt in dirts:
        #     screen.blit(dirt_skin, dirt)  # desenha a sujeira

        self.draw_grid()

        for entity in entities:
            entity.render(self.screen)

        self.score_font = self.font.render('Score: %s' % score, True, (255, 255, 255))
        self.screen.blit(self.score_font, self.score_rect)  # desenha o score

    def show_screen(self, width, message):
        while True:
            game_over_font = pygame.font.Font('freesansbold.ttf', 75)
            game_over_screen = game_over_font.render(message, True, (255, 255, 255))
            game_over_rect = game_over_screen.get_rect()
            game_over_rect.midtop = (width / 2, 10)
            self.screen.blit(game_over_screen, game_over_rect)
            pygame.display.update()
            pygame.time.wait(500)
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit(0)
                    if hasattr(event, 'key') and event.key == K_ESCAPE:
                        exit(0)