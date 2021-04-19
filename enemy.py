from utils import *
import pygame
import math


enemy_imgs = {
    'scorpion': {
        'run': [
            load_img(f'f/enemies/scorpion/1_enemies_1_run_{i:0>3}.png', size=(0.6, 0.6), flip=(True, False))
            for i in range(20)
        ],
    }
}


def open_path(file: str, code: str = 'all'):  # FIXME
    r = {'path': [], 'characters': []}
    f_way = open_file(file)
    label = 'path' if code == 'one.v.1' else ''
    for line in f_way:
        if line[0] == '!':
            label = line[1:-1]
        else:
            try:
                r[label].append(tuple(map(int, line.split())))
            except:
                r[label].append(tuple(line.split()))
    return r


class Wave:
    def __init__(self, path: str, delay: int, code: str = 'wave.v.1', start: int = 0):
        p = open_path(path, code)

        self.path = p['path']
        self.characters = p['characters']
        self.character_num = 0
        self.character_i = 0

        self.start = start
        self.delay = delay
        self.adding = False
        self.stop = False
        self.t = 0

    def update(self, output: list):
        if self.stop:
            return

        self.t += 1

        if not self.adding:
            if self.t >= self.start:
                self.adding = True
                self.t = 0
            return

        if self.t % self.delay == 0:
            i = self.character_i
            settings = self.characters[i]
            output.append(Enemy(self.path, settings[2], enemy_imgs[settings[1]]))
            self.character_num += 1

            if self.character_num == settings[0]:
                self.character_num = 0
                self.character_i += 1
                if i + 1 >= len(self.characters):
                    self.stop = True
                    self.adding = False


class Enemy:
    def __init__(self, path, start_group, imgs_groups):
        self.img_ind = 0
        self.img_group = start_group
        self.imgs_groups = imgs_groups

        self.path = path['path']
        self.t = 0
        self.pos = path['path'][0]

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
