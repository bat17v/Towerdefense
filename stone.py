from utils import *
import pygame

stone_imgs = {
    'stone': [load_img(f'f/towers/stones/{i}.png') for i in range(40, 45)]
}


class Stone:
    def __init__(self, x: int, y: int, v: int, imgs: list):
        self.pos = x, y
        self.good = True

        self.step = 0
        self.t = 0

        self.a = 0.5
        self.v_x = 0
        self.v_y = v

        self.img = imgs[0] if len(imgs) > 0 else pygame.Surface((0, 0))
        self.img_i = 0
        self.imgs = imgs

    def draw(self, screen: pygame.SurfaceType):
        if self.good:
            screen.blit(self.img, self.pos)

    def hit(self, x, y):
        x1, y1 = self.pos
        x2, y2 = x, y
        t = 40

        self.v_x = (x2 - x1) / t
        self.v_y = (y2 - y1 - self.a * t * t / 2) / t

        self.t = t
        self.step += 1

    def update(self):
        if self.step == 0:
            self.pos = self.pos[0], self.pos[1] + self.v_y
        elif self.step == 1:
            self.t -= 1
            if self.t < 0:
                self.step += 1

            self.v_y += self.a

            x, y = self.pos
            x += self.v_x
            y += self.v_y
            self.pos = x, y

        elif self.step == 2:
            self.img_i += 1
            if self.img_i >= len(self.imgs):
                self.good = False
                self.step += 1
                return

            x, y = self.pos

            center_x = x + self.img.get_width() // 2
            center_y = y + self.img.get_height() // 2

            self.img = self.imgs[self.img_i]

            x = center_x - self.img.get_width() // 2
            y = center_y - self.img.get_height() // 2

            self.pos = x, y
