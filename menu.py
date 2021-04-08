import pygame


class Button:
    def __init__(self, x: int, y: int, img: pygame.SurfaceType, cost: int = 0):
        self.pos = x, y
        self.rect = pygame.Rect(x, y, *img.get_size())
        self.img = img
        self.cost = cost

    def draw(self, screen: pygame.SurfaceType):
        screen.blit(self.img, self.pos)

    def action(self):


    def update(self, x: int, y: int):
        if self.rect.collidepoint(*self.pos):
            self.action()
