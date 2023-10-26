import pygame

def get_mouse_cell(cells,cell_size):
    x,y = pygame.mouse.get_pos()
    x = int(x//cell_size)
    y = int(y//cell_size)
    c = cells[y][x]
    return c

def distance(c1,c2):
    return abs(c1.x-c2.x) + abs(c1.y-c2.y)