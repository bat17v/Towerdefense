import pygame
import sys, os


def resource_path(relative_path: str):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_img(file_name: str, size: tuple = (None, None), flip: tuple = (False, False)):
    img = pygame.image.load(resource_path(file_name))

    return transform_img(img, size, flip)


def transform_img(img, size: tuple = (None, None), flip: tuple = (False, False), square=None):

    if type(size[0]) == int and type(size[1]) == int:
        img = pygame.transform.scale(img, size)
    if type(size[0]) == float and type(size[1]) == float:
        x, y = img.get_size()
        img = pygame.transform.scale(img, (int(size[0] * x), int(size[1] * y)))

    if type(square) == int:
        m = max(size)
        s0 = size[0] / (m / square)
        s1 = size[1] / (m / square)
        img = pygame.transform.scale(img, (int(s0), s1))
    img = pygame.transform.flip(img, flip[0], flip[1])
    return img


def open_file(file_name: str):
    return open(resource_path(file_name))
