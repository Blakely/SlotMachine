import pygame, sys, random
from pygame.locals import *

#initialize pygame
pygame.init()

DISPLAY_SIZE = (600,386)
DISPLAY_TEXT = 'Slot Machine'
COLOR_BLACK = (255,255,255)
IMAGE_PATH = 'images'
IMG_EXT = '.png'
IMAGE_BG = 'machine' + IMG_EXT

#associative array for reel bet multipliers
REELS_X = (0,1,1,2,3,5,10)

NUM_REELS = REELS_X.length


#gets a random number
def getRandom(maxNum):
    return random.randint(0,maxNum-1)

#spins the reel (returns random numbers)
def spin(numReels,maxNum):
    reels = list()
    
    #loop through all the required numbers
    for reel in range(0,numReels):
        reels.append(getRandom(maxNum))
    
    return reels;

#draws an image
def drawImage(screen,imgFile,dest=(0,0)):
    img = pygame.image.load(imgFile)
    
    screen.blit(img,dest)
    pygame.display.flip()

#redraws the game screen
def drawGame(screen):
    screen.fill(COLOR_BLACK)
    
# main game loop
def game(screen):
    while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            #get the mouse coordinates
            #print even.pos()
            #mX = event.pos()
            #mY
    drawImage(screen,IMAGE_BG)
    pygame.display.update()

#main program - sets up pygame & starts game
def main():
    #setup game screen
    gameScreen = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption(DISPLAY_TEXT)
    
    #start the game
    game(gameScreen);

#Start program
if __name__ == "__main__":
    main()