import pygame as pg
from tire import Tire


class Car(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, position: list, tires: Tire):
        pg.sprite.Sprite.__init__(self)
        self.image: pg.Surface = image
        self.position: list = position
        self.rotation: float = 0.0  # 0-359
        self.tires = tires
        self.rect = self.image.get_rect(center=self.position)

        self.acceleration: float = 0
        self.velocity: float = 0.0
        self.rotation_speed: float = 0.0
        self.distance_driven: float = 0.0  # The distance driven with the current tires, used for tire health bar
        self.can_pit = False
        self.collision_sound_played = False

    def render(self, screen: pg.Surface):
        rotated_model = pg.transform.rotate(self.image, self.rotation)
        self.rect = rotated_model.get_rect(center=self.position)
        screen.blit(rotated_model, self.rect)
