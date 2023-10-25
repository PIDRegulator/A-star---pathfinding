import pygame

class cell:
    def __init__(self,x,y,size,wall=False):
        self.x = x
        self.y = y
        self.size = size

        self.g_cost = 0 # Position from start
        self.h_cost = 0 # Position to end
        self.f_cost = 0 # g_cost + h_cost

        self.wall = wall

        if wall:
            self.color = (0,0,0)
        else:
            self.color = (255,255,255)
    
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,[self.x*self.size,self.y*self.size,self.size,self.size])