import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 588))
img = pygame.image.load('f/enemies/scorpion/1_enemies_1_run_001.png')

screens = [
    pygame.transform.scale(pygame.image.load('f/screens/screen0.png'), (1000, 588))
]
path = list()
size_x = img.get_width() // 2
size_y = img.get_height() // 2

while True:
    screen.blit(screens[0], (0, 0))
    pygame.time.delay(10)

    x, y = pygame.mouse.get_pos()
    x -= size_x
    y -= size_y

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.MOUSEBUTTONUP:
            print(x, y)
            path.append((x, y))

    for x_i, y_i in path:
        screen.blit(img, (x_i, y_i))

    screen.blit(img, (x, y))

    pygame.display.flip()
