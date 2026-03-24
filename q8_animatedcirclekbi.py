import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")

x, y = width // 2, height // 2
radius = 30
speed = 5

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, (255, 105, 180), (x, y), radius)  
    pygame.display.flip()

pygame.quit()
sys.exit()
