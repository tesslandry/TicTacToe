#Display

import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Tic Tac Toe')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        screen.fill((0,255,255))
        pygame.display.flip()