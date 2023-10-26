import pygame

class cell:
    def __init__(self,x,y,size,block_type=0):
        self.x = x
        self.y = y
        self.size = size

        self.g_cost = 0 # Position from start
        self.h_cost = 0 # Position to end
        self.f_cost = 0 # g_cost + h_cost

        self.block_type = block_type
        self.colors = [(255,255,255),(0,0,0),(0,255,0),(255,0,0)]

    def draw(self,screen):
        color = self.colors[self.block_type]
        pygame.draw.rect(screen,color,[self.x*self.size,self.y*self.size,self.size,self.size])

        
    