import pygame
import time
import sys
from pygame.sprite import Group
from wallsANDroads import Wall, Road
from mazesettings import Settings
import functions as f
from player import Player


def run_maze():
    
    pygame.init()
    
    settings = Settings()
    
    pygame.display.set_caption("Maze")
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    
              
    player = Player(settings, screen)
    
    maze_number = 1
    
    while True:
        
        
        f.start_menu(screen, settings)
            
            
            

        
        maze = f.generatemaze(settings.maze_height, settings.maze_width)
        minimum_steps = f.minimum_steps(maze, settings.maze_width, settings.maze_height)
        
        start_x = maze[-1].index('a') * settings.wall_width
        player.rect.topleft = (start_x, settings.screen_height - settings.wall_height)
        
        walls = Group()
        roads = Group()
        
        f.create_maze(maze, settings, screen, walls, roads)
            
    
    
        while True:
            
            f.draw_maze(walls, roads)
            f.check_events(player, walls, settings, screen)
        
            player.draw_player()
            f.show_number_of_steps(screen, settings, player)
            f.to_pause(screen, settings)
            f.show_points(screen, settings, player)
            
            if player.rect.top < 0:
                
                additional_points = f.calculate_points(player, minimum_steps)
                player.points += additional_points
                        
                f.maze_finished(screen, settings, player, additional_points, maze_number)
                maze_number += 1
                
                break
        
            pygame.display.flip()
    
    
run_maze()