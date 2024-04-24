import pygame
from pygame.sprite import Sprite
import random


class Wall(Sprite):
    
    def __init__(self, x, y, settings, screen, wall_pic):
        
        super(Wall, self).__init__()
        
        walls_pictures = {1: 'Castle_Wall.jpg', 2: 'blue_wall.png', 3: 'Dungeon_Wall.png'}
        
        
        self.x = x
        self.y = y
        
        self.image = pygame.image.load(walls_pictures[wall_pic])
        self.image = pygame.transform.scale(self.image, settings.cell_size)
        
        
        
        self.screen = screen
        
        self.rect = pygame.Rect(x, y, settings.wall_width, settings.wall_height)
        
    def draw_wall(self):
        
        self.screen.blit(self.image, self.rect)
        
        
        
class Road(Sprite):
    
    def __init__(self, x, y, settings, screen, road_pic):
        
        super(Road, self).__init__()
        
        roads_pictures = {1: 'b7c092bb30a000ddc7d142d2a0cdf731.jpg', 2: 'dirt_0.png', 3: '1000_F_407541294_A8o5pW1SPNBIENxt6Jsttpw5o2NsIWRJ.jpg'}
        
        self.x = x
        self.y = y
        
        self.image = pygame.image.load(roads_pictures[road_pic])
        self.image = pygame.transform.scale(self.image, settings.cell_size)
        
        
        
        self.screen = screen
        
        self.rect = pygame.Rect(x, y, settings.wall_width, settings.wall_height)
        
    def draw_road(self):
        
        self.screen.blit(self.image, self.rect)