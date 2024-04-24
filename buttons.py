import pygame

class Description_button:
    
    def __init__(self, screen, settings):
        self.button_pressed = False
        self.font = pygame.font.Font(None, 72)
        self.button_text = self.font.render('How to play', True, (0, 0, 0))
        self.button_rect = self.button_text.get_rect()
        screen_rect = screen.get_rect()
        self.button_rect.center = (screen_rect.centerx, screen_rect.centery + 75)
        
        self.button_color = (230, 230, 230)

    
    def draw_button(self, screen, settings):
        pygame.draw.rect(screen, self.button_color, self.button_rect)
        screen.blit(self.button_text, self.button_rect)
            
class Exit_description_button:
    
    def __init__(self, screen, settings):
        
        self.font = pygame.font.Font(None, 72)
        self.button_text = self.font.render('Exit', True, (0, 0, 0))
        self.button_rect = self.button_text.get_rect()
        screen_rect = screen.get_rect()
        self.button_rect.center = (settings.screen_width/12 + 50, screen_rect.centery + 160)

    
    def draw_button(self, screen, settings):
        pygame.draw.rect(screen, (239, 230, 230), self.button_rect)
        screen.blit(self.button_text, self.button_rect)
        
class Start_the_game_button:
    
    def __init__(self, screen, settings):
        
        self.button_color = (230, 230, 230)
        
        self.font = pygame.font.Font(None, 72)
        self.button_text = self.font.render('Start the game', True, (0, 0, 0))
        self.button_rect = self.button_text.get_rect()
        screen_rect = screen.get_rect()
        self.button_rect.center = screen_rect.center

    
    def draw_button(self, screen, settings):
        pygame.draw.rect(screen, self.button_color, self.button_rect)
        screen.blit(self.button_text, self.button_rect)