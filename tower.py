from utils import *
from stone import *
import pygame


tower_imgs = {
    'stone': [
        [load_img(f'f/towers/stone_towers/{i}.png', size=(0.8, 0.8)) for i in [1, 3, 2]],
        [load_img(f'f/towers/stone_towers/{i}.png', size=(0.8, 0.8)) for i in [1, 6, 2]],
        [load_img(f'f/towers/stone_towers/{i}.png', size=(0.8, 0.8)) for i in [4, 7, 5]]
    ]
}


class Tower:
    def __init__(self, x: int, y: int):
        self.pos = x, y

    def draw(self, screen: pygame.SurfaceType):
        pass

    def update(self):
        pass


class StoneTower(Tower):
    def __init__(self, x: int, y: int, stone: list, imgs: list):
        super().__init__(x, y)

        self.stones = list()
        self.stone_imgs = stone

        self.pos_platform = 1
        self.move_platform = 5

        self.imgs = imgs
        self.level = 0

    def draw(self, screen: pygame.SurfaceType):
        p = self.pos_platform
        x, y = self.pos

        screen.blit(self.imgs[self.level][0], (x,  y + p))
        screen.blit(self.imgs[self.level][1], self.pos)
        screen.blit(self.imgs[self.level][2],
                    (x, y + p + self.imgs[self.level][0].get_height() - 3))

        for stone in self.stones:
            stone.draw(screen)

    def update(self):
        p = self.pos_platform
        x, y = self.pos
        i = self.imgs[self.level]

        for stone in self.stones:
            stone.update()

        if p <= 0 or p >= i[1].get_height() - i[0].get_height() * 3 - 10:
            self.move_platform *= -1
            if self.move_platform < 0:
                self.stones.append(Stone(x + i[0].get_width() // 2 - self.stone_imgs[0].get_width() // 2, y + p,
                                         self.move_platform, self.stone_imgs))
            else:
                self.stones[-1].hit(x + 150, y + 150)
        self.pos_platform += self.move_platform


class SupportTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        pass
