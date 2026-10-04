import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Random Ball")

x, y = 250, 250 # ball beech me

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Yaha tera random pattern
    x += random.randint(-5, 5) # -5 se 5 tak random move
    y += random.randint(-5, 5)

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
    pygame.display.update()
    
    pygame.time.delay(30) # ye tera time.sleep hai pygame me

pygame.quit()