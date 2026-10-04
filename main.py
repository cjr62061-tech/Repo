import pygame
import random

pygame.init()
# Android ke liye full screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = screen.get_size()
pygame.display.set_caption("Random Ball")

x, y = W//2, H//2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            running = False # touch karte hi band

    x += random.randint(-10, 10)
    y += random.randint(-10, 10)

    # screen se bahar na jaye
    x = max(20, min(W-20, x))
    y = max(20, min(H-20, y))

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 40)
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()