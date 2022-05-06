import pygame
from pygame.surface import SurfaceType

from game_rules import *


class SpriteSheet:
    """Extraído de https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/#a-simple-sprite-sheet"""

    def __init__(self, filename):
        """Carrega a spritesheet"""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Não foi possível carregar a spritesheet: {filename}")
            raise SystemExit(e)

    def image_at(self, rectangle: tuple, colorkey=None):
        """
        Carrega um retângulo de uma imagem.

        :param rectangle: (x, y, x+offset, y+offset)
        :param colorkey:
        :return: o retângulo carregado
        """

        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects: list, colorkey: int = None):
        """Carrega vários retângulos e os retorna como uma lista."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey: int = None):
        """Carrega uma linha de imagens, e as retorna como uma lista."""
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


class CollisionBox(object):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def collides_with(self, other):
        if (self.x < other.x + other.width) and \
                (self.x + self.width > other.x) and \
                (self.y < other.y + other.height) and \
                (self.y + self.height > other.y):
            return True
        return False


class Entity(object):

    def __init__(self, x: int, y: int, collision_box: CollisionBox):
        self.x = x
        self.y = y
        self.collision_box = collision_box

    def collides_with(self, other):
        """
        Checa se a entidade atual está em colisão com outra entidade.

        :param other: A outra entidade.
        :type other: Entity
        :return: True se ambas entidades colidem, False se não
        """

        # TODO fazer verificação para ver se saiu da tela
        return self.collision_box.collides_with(other.collision_box)

    def render(self, screen):
        """
        Renderiza a entidade atual na tela.
        """
        pass


class Player(Entity):
    def __init__(self, x: int, y: int, collision_box: CollisionBox):
        super().__init__(x, y, collision_box)
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.clock = 0
        states = SpriteSheet('images/Kirby.png')
        # Create a black king.
        self.neutral_state_image = states.image_at((6, 24, 15, 15))
        self.blinking_state_image = states.image_at((26, 24, 15, 15))
        self.image = self.neutral_state_image
        self.rect = self.image.get_rect()

    def move(self, my_direction: int):
        """
        Move o jogador na direção desejada.

        :param my_direction: A direção pressionada
        """
        if my_direction is None:
            self.clock = (self.clock + 1) % 20
            if 15 < self.clock <= 20:
                self.image = self.blinking_state_image
            else:
                self.image = self.neutral_state_image

        x_increment = 0
        y_increment = 0

        if my_direction == DIR_UP:
            y_increment = -grid_size
        if my_direction == DIR_DOWN:
            y_increment = grid_size
        if my_direction == DIR_RIGHT:
            x_increment = grid_size
        if my_direction == DIR_LEFT:
            x_increment = -grid_size

        self.x += x_increment
        self.y += y_increment

    def render(self, screen: SurfaceType):
        """
        Mostra o personagem na tela.
        """
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        screen.blit(self.image, self.rect)
