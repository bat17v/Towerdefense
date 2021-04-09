import pygame
from utils import *


menu_imgs = {
    'buttons': {
        'touch': [load_img(f'ico_{i + 1}.png') for i in range(25)],
        'cost': load_img('ico_cost.png'),
    },
    'panel': pygame.image.load('panel.png'),
}


class Button:
    def __init__(self, x: int, y: int, img: pygame.SurfaceType, cost: int = 0):
        self.pos = x, y
        self.rect = pygame.Rect(x, y, *img.get_size())
        self.img = img
        self.cost = cost

    def draw(self, screen: pygame.SurfaceType):
        screen.blit(self.img, self.pos)

    def action(self):
        pass  # TODO: реализовать создание действия кнопки

    def update(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            self.action()


class Panel:
    def __init__(self, x: int, y: int, img: pygame.SurfaceType, buttons: list = None):
        self.pos = x, y
        self.rect = pygame.Rect(x, y, *img.get_size())
        self.img = img
        self.buttons = buttons

    def draw(self, screen: pygame.SurfaceType):
        screen.blit(self.img, self.pos)
        for button in self.buttons:
            button.draw()

    def update(self, x: int, y: int):
        for button in self.buttons:
            button.update(x, y)
