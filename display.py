#Display

import pygame
import sys
import board
pygame.init()

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN  = (0, 255, 255)

#DISPLAY
pygame.display.set_caption('Tic Tac Toe')
SCREEN_WIDTH = 800
SCREEN_SIZE = (800, 800)
BACKGROUND_COLOR = CYAN


screen = pygame.display.set_mode(SCREEN_SIZE)

def drawBoard():
        screen.fill(BACKGROUND_COLOR)

        #We want our board to draw based on screen size
        #We want margins on the outside
        spacing = SCREEN_WIDTH / 5
        lineLength = spacing*3

        #Vertical Lines
        pygame.draw.line(screen, BLACK, (spacing*2, spacing), (spacing*2, (spacing + lineLength)), 2)
        pygame.draw.line(screen, BLACK, (spacing*3, spacing), (spacing*3, (spacing + lineLength)), 2) 
        #Horizontal Lines
        pygame.draw.line(screen, BLACK, (spacing, spacing*2), ((spacing + lineLength), spacing*2), 2)
        pygame.draw.line(screen, BLACK, (spacing, spacing*3), ((spacing + lineLength), spacing*3), 2)      


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        drawBoard()

        pygame.display.flip()