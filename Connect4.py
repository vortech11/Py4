import pygame
import os

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

positions = []

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        positions.append(1)
                    if event.key == pygame.K_2:
                        positions.append(2)
                    if event.key == pygame.K_3:
                        positions.append(3)
                    if event.key == pygame.K_4:
                        positions.append(4)
                    if event.key == pygame.K_5:
                        positions.append(5)
                    if event.key == pygame.K_6:
                        positions.append(6)
                    if event.key == pygame.K_7:
                        positions.append(7)
        
    os.system('cls')
    print(positions)
    
    window.fill(0)
    for x in range(0, len(positions), 2):
        rect = pygame.Rect(0, 0, 50, 50)
        rect.x = positions[x] * 50
        rect.y = 250
        pygame.draw.rect(window, 999, rect)
    pygame.display.flip()

pygame.quit()
exit()