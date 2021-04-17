import pygame
from utils import *


menu_imgs = {
    'buttons': {
        'ico': [load_img(f'f/buttons/ico_{i + 1}.png', size=(0.50556, 0.50556)) for i in range(23)],
        'action': {action: load_img(f'f/buttons/actions/{action}.png', size=(0.50556, 0.50556)) for action in ('faster', 'pause')}
    },
    'panel': load_img('f/buttons/panel.png', size=(0.50556, 0.50556)),
    'cost': load_img('f/buttons/ico_cost.png', size=(0.50556, 0.50556)),
}


class Button:
    def __init__(self, x: int, y: int, img: pygame.SurfaceType, command=lambda: None, cost: int = 0):
        self.pos = x, y
        self.rect = pygame.Rect(x, y, *img.get_size())
        self.img = img
        self.cost = cost
        self.command = command

    def draw(self, screen: pygame.SurfaceType):
        screen.blit(self.img, self.pos)

    def try_push(self, x: int, y: int):
        if self.rect.collidepoint(x, y):
            self.command()


class Panel:
    def __init__(self, x: int, y: int, img: pygame.SurfaceType, buttons=None):
        if buttons is None:
            buttons = []
        self.pos = x, y
        self.rect = pygame.Rect(x, y, *img.get_size())
        self.img = img
        self.buttons = buttons

    def draw(self, screen: pygame.SurfaceType):
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)
        screen.blit(self.img, self.pos)
        for button in self.buttons:
            button.draw(screen)

    def try_push(self, x: int, y: int):
        for button in self.buttons:
            button.try_push(x, y)
