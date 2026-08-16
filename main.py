# two player chess in python with pygame
# part one, set up variables images and game loop 

import pygame 

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60 
# Game variables and images 

# main game loop 
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray') # Background color 
    
    for event in pygame.event.get(): # gets keyboard, mouse, etc from computer 
        