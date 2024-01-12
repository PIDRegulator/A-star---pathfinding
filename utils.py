import pygame

def get_mouse_cell(cells,cell_size):
    x,y = pygame.mouse.get_pos()
    x = int(x//cell_size)
    y = int(y//cell_size)
    c = cells[y][x]
    return c

def distance(c1,c2):
    return abs(c1.x-c2.x) + abs(c1.y-c2.y)

def astar(cells, start, end):
    visited = set()
    queue = [start]

    while queue:
        c, queue, visited =  astar_step(cells, end, queue, visited)
        if c:
            return True
    return False

def astar_step(cells, end, queue, visited = set(), color_visited = False):
    current = queue.pop(0)
    print(current.x, current.y)
    if current == end:
        return True, None, None
    visited.add(current)
    if color_visited and current.block_type != 2:
        current.block_type = 5
    for neighbor in current.get_neighbours(cells):
        if neighbor not in visited and neighbor.block_type != 1:
            if neighbor.parent != None:
                if neighbor.parent.g_cost <= current.g_cost:
                    continue
            neighbor.parent = current
            neighbor.g_cost = current.g_cost + 1
            neighbor.h_cost = distance(neighbor,end)
            neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
            queue.append(neighbor)
            if neighbor.block_type not in [2, 3]:
                neighbor.block_type = 6

    queue.sort(key=lambda x: (x.f_cost, x.h_cost, x.x, x.y))
    return False, queue, visited

def reconstruct_path(start, end):
    current = end
    while current != start:
        if current != end:
            current.block_type = 4
        current = current.parent

def clear(cells, everything=True):
    for row in cells:
        for c in row:
            c.parent = None
            if everything:
                c.block_type = 0
            if c.block_type == 4:
                c.block_type = 0

