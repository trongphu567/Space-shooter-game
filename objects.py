import pygame
import os

WIDTH, HEIGHT = 700, 670
class Background():
    def __init__(self, win):
        self.win = win
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()

        self.reset()
        self.move = True

    def update(self, speed):
        if self.move:
            self.y1 += speed
            self.y2 += speed

            if self.y1 >= HEIGHT:
                self.y1 = -HEIGHT  
            if self.y2 >= HEIGHT:
                self.y2 = -HEIGHT

        self.win.blit(self.image, (self.x,self.y1))  
        self.win.blit(self.image, (self.x,self.y2)) 
         
    def reset(self):
        self.x = 0
        self.y1 = 0
        self.y2 = -HEIGHT
                 
                
                 