from utils import *
from enemy import *
from tower import *
from menu import *


pygame.init()
screen = pygame.display.set_mode((1000, 588))  # TODO: увеличить высоту для панели
screens = [
    load_img('f/screens/screen0.png', size=(1000, 588))
]
world = [
    Enemy(open_path('f/levels/paths/level_1.2.txt'), 'run', enemy_imgs['scorpion']),
    StoneTower(200, 200, stone_imgs['stone'], tower_imgs['stone'])
]
t = 0
# TODO: нужно создать кнопки и панель соответствующих классов
while True:
    screen.blit(screens[0], (0, 0))
    pygame.time.delay(10)
    t += 1
    if t % 150 == 0:
        world.append(Enemy(open_path('f/levels/paths/level_1.2.txt'), 'run', enemy_imgs['scorpion']))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    for elem in world:
        elem.update()
        elem.draw(screen)

    pygame.display.flip()
