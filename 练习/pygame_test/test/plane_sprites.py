import pygame


class GameSprites(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = pygame.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

