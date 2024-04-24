import pygame

class Player():
    
    def __init__(self, settings, screen):
        
        self.screen = screen
        self.settings = settings
        
        self.image = pygame.image.load('spr_minotaur_design.png')
        self.image = pygame.transform.scale(self.image, settings.cell_size)
        self.image.set_colorkey((255, 255, 255))
        
        self.rect = self.image.get_rect()
        
        self.screen_rect = screen.get_rect()
        
    
        self.step_counter = 0
        self.points = 0

        
        
    def draw_player(self):
        
        self.screen.blit(self.image, self.rect)