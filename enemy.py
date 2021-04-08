from utils import *
import pygame
import math
pygame.K_a

enemy_imgs = {
    'scorpion': {
        'run': [
            load_img(f'f/enemies/scorpion/1_enemies_1_run_{i:0>3}.png', size=(0.6, 0.6), flip=(True, False))
            for i in range(20)
        ],
    }
}


def open_path(file: str):
    r = []
    f_way = open_file(file)
    label = ''
    for line in f_way:

        r.append(tuple(map(int, line.split())))
    return r


class Wave:
    def __init__(self, path: str, delay: int, start: int = 0):
        p = open_path(path)
        self.path = p['path']
        self.characters = p['characters']
        self.character_num = 0
        self.cheracter_i = 0

        self.start = start
        self.delay = delay
        self.adding = False
        self.t = 0

    def update(self, output: list):
        self.t += 1

        if not self.adding:
            if self.t >= self.start:
                self.adding = True
                self.t = 0
            return

        if self.t % self.delay == 0:
            output.append(Enemy(self.path, self.characters[self.c]))


class Enemy:
    def __init__(self, path, start_group, imgs_groups):
        self.img_ind = 0
        self.img_group = start_group
        self.imgs_groups = imgs_groups

        self.path = path
        self.t = 0
        self.pos = path[0]

        self.rect = imgs_groups[start_group][0].get_rect()

    def draw(self, screen):
        screen.blit(self.imgs_groups[self.img_group][self.img_ind], self.pos)

    def update(self):
        self.img_ind = (self.img_ind + 1) % len(self.imgs_groups[self.img_group])
        self.rect = self.imgs_groups[self.img_group][self.img_ind].get_rect()

        if self.t == len(self.path) - 1:
            return False

        start_x, start_y = self.pos

        x1, y1 = self.path[self.t]
        x2, y2 = self.path[self.t + 1]

        dir_x, dir_y = x2 - x1, y2 - y1
        len_dir = math.sqrt(dir_x * dir_x + dir_y * dir_y)
        dir_x /= len_dir
        dir_y /= len_dir

        end_x, end_y = self.pos = start_x + dir_x, start_y + dir_y
        self.rect.x, self.rect.y = self.pos

        if (start_x <= x2 <= end_x or start_x >= x2 >= end_x) or \
                (start_y <= y2 <= end_y or start_y >= y2 >= end_y):
            self.t += 1

        return True
