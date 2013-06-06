import pygame, sys, random
from pygame.locals import *

pygame.init()

DISPLAY_SIZE = (600,386)
DISPLAY_TEXT = 'Slot Machine'
COLOR_BLACK = (255,255,255)
IMAGE_PATH = 'images\\'
IMG_EXT = '.png'
IMAGE_BG = 'bg' + IMG_EXT

#draws the background image
def drawImage(screen,imgFile,dest=(0,0)):
    img = pygame.image.load(imgFile)

    screen.fill(COLOR_BLACK)
    screen.blit(img,dest)
    pygame.display.flip()

# main game loop
def game(screen):
    while True:
        for event in pygame.event.get():
            print event.type
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        drawImage(screen,IMAGE_PATH + IMAGE_BG)
        pygame.display.update()

#main program - sets up pygame & starts game
def main():
    gameScreen = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption(DISPLAY_TEXT)
    
    game(gameScreen);

#Start program
if __name__ == "__main__":
    main()