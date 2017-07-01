import pygame
import time

class Map():
    def __init__(self):
        self.screen_size = (800,480)
        pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.mouse.set_visible(False)

    def init_screen(self):
        #Vars
        self.bgcolor = (44,62,80)
        self.squaresize = 350
        self.squarecolor = (149,165,166)

        #Überschrift
        self.screen.fill(self.bgcolor)
        self.screen.blit(pygame.font.SysFont('Comic Sans MS', 50).render('Indoor Positioning System', False, (230, 126, 34)),(190,5))

        #Legende
        self.screen.blit(pygame.image.load('little_twitterlogo.png'),(100,430))
        self.screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(' = deine Position', False, (230, 126, 34)),(130,430))

        pygame.draw.rect(self.screen, self.squarecolor, ((self.screen_size[0]/2-(self.squaresize/2)), (self.screen_size[1]/2-(self.squaresize/2)),self.squaresize,self.squaresize),7)
        pygame.display.update()

    def setObj(self, x, y):
        #Const
        new_x = x + (self.screen_size[0]/2-(self.squaresize/2))
        new_y = y + (self.screen_size[1]/2-(self.squaresize/2))

        #Bildsirm leeren
        self.init_screen()

        self.screen.blit( pygame.image.load('little_twitterlogo.png'), (new_x,new_y))
        pygame.display.update()
