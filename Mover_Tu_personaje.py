import pygame
import sys

from battle_escene import main

pygame.init()
size = (800, 500)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

DARK_VIOLET = (75, 0, 108)
WHITE = (255, 255, 255)

step_count = 0

pygame.mouse.set_visible(False)

cord_x = 10
cord_y = 10

x_speed = 0
y_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            step_count = step_count + 1
            x_speed = -3
        if event.key == pygame.K_RIGHT:
            step_count = step_count + 1
            x_speed = 3
        if event.key == pygame.K_UP:
            step_count = step_count + 1
            y_speed = -3
        if event.key == pygame.K_DOWN:
            step_count = step_count + 1
            y_speed = 3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            x_speed = 0
        if event.key == pygame.K_RIGHT:
            x_speed = 0
        if event.key == pygame.K_UP:
            y_speed = 0
        if event.key == pygame.K_DOWN:
            y_speed = 0

    # mouse_pos = pygame.mouse.get_pos()
    # x = mouse_pos[0]
    # y = mouse_pos[1]
    screen.fill(WHITE)
    cord_x += x_speed
    cord_y += y_speed

    pygame.draw.rect(screen, DARK_VIOLET, (cord_x, cord_y, 50, 50))
    if step_count == 100:
        main()
    print(step_count)
    pygame.display.flip()
    clock.tick(60)
