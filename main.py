from utils import *
from enemy import *
from tower import *
from menu import *


def pause_game():
    global play
    play = not play


pygame.init()
screen = pygame.display.set_mode((1000, 588 + int(192 * 0.50556)))  # TODO: увеличить высоту для панели
play = True
screens = [
    load_img('f/screens/screen0.png', size=(1000, 588))
]
world = [
    Enemy(open_path('f/levels/paths/level_1.2.txt'), 'run', enemy_imgs['scorpion']),
    StoneTower(200, 200, stone_imgs['stone'], tower_imgs['stone'])
]
t = 0

buttons = [
    Button(881, 560, menu_imgs['buttons']['action']['pause'], pause_game)
]
p = Panel(0, 588, menu_imgs['panel'], buttons)
while True:
    if play:
        screen.blit(screens[0], (0, 0))
        pygame.time.delay(10)
        t += 1
        if t % 150 == 0:
            world.append(Enemy(open_path('f/levels/paths/level_1.2.txt'), 'run', enemy_imgs['scorpion']))

        for elem in world:
            elem.update()
            elem.draw(screen)

        p.draw(screen)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.MOUSEBUTTONUP:
            p.try_push(*pygame.mouse.get_pos())

    pygame.display.flip()
