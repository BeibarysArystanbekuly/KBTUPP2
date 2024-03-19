import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)
RED = (255, 0, 0)


radius = 25
x = screen_width // 2
y = screen_height // 2
speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - speed >= 0:
                    y -= speed
            elif event.key == pygame.K_DOWN:
                if y + speed <= screen_height:
                    y += speed
            elif event.key == pygame.K_LEFT:
                if x - speed >= 0:
                    x -= speed
            elif event.key == pygame.K_RIGHT:
                if x + speed <= screen_width:
                    x += speed

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
