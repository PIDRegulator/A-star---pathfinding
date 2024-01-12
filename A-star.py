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

queue = []
visited = set()

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
                    path_exist = utils.astar(cells,start,end)
                    if path_exist:
                        print("Path found")
                        utils.reconstruct_path(start,end)
                    else:
                        print("Path not found")

            elif event.key == pygame.K_KP_0:
                if len(queue) == 0:
                    queue = [start]
                    visited = set()
                completed, queue, visited = utils.astar_step(cells,end,queue, set(), True)
                if completed:
                    for row in cells:
                        for c in row:
                            if c.block_type in [5,6]:
                                c.block_type = 0
                    utils.reconstruct_path(start,end)
                    queue = [start]
                    visited = set()
            if event.key == pygame.K_KP_1:
                utils.clear(cells, True)
                start = None
                end = None    
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            utils.clear(cells, False)
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