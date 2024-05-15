import pygame as pg


class Barricade(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, position: list):
        pg.sprite.Sprite.__init__(self)
        self.image: pg.Surface = image
        self.position: list = position
        self.rect = self.image.get_rect(center=self.position)

    def render(self, screen: pg.Surface):
        self.rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, self.rect)
