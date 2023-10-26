import pygame
import random
import time
import utils
from cell import cell

pygame.init()
pygame.display.set_caption("A*")
clock = pygame.time.Clock()

screen_size_pixels = 1000
board_size = 10
cell_size = (screen_size_pixels/board_size)
start = None
end = None

print(cell_size)

screen_size = (screen_size_pixels, screen_size_pixels)
screen = pygame.display.set_mode((screen_size[0],screen_size[1]))
cells = []

for i in range(board_size):
    row = []
    for j in range(board_size):
        c = cell(j,i,cell_size)
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                if start and end:
                    print(utils.distance(start,end))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                c = utils.get_mouse_cell(cells,cell_size)
                if c == start:
                    start = None
                if c == end:
                    end = None
                if c.block_type == 0:
                    c.block_type = 1
                else:
                    c.block_type = 0
            elif event.button == 3:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LSHIFT]:
                    if end:
                        end.block_type = 0
                    end = utils.get_mouse_cell(cells,cell_size)
                    end.block_type = 3
                    if end == start:
                        start = None
                else:
                    if start:
                        start.block_type = 0
                    start = utils.get_mouse_cell(cells,cell_size)
                    start.block_type = 2
                    if start == end:
                        end = None

    pygame.display.flip()  