import pygame
import random
import time
from cell import cell

pygame.init()
pygame.display.set_caption("A*")
clock = pygame.time.Clock()

screen_size_pixels = 1000
board_size = 10
cell_size = (screen_size_pixels/board_size)

print(cell_size)

screen_size = (screen_size_pixels, screen_size_pixels)
screen = pygame.display.set_mode((screen_size[0],screen_size[1]))
cells = []

for i in range(board_size):
    row = []
    for j in range(board_size):
        wall = random.choice([True,False])
        c = cell(j,i,cell_size,wall)
        row.append(c)
    cells.append(row)

while True:
    screen.fill((255,255,255))
    for row in cells:
        for c in row:
            c.draw(screen)
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()  