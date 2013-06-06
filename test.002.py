import pygame, sys, random
from pygame.locals import *

#initialize pygame
pygame.init()

DISPLAY_SIZE = (600,386)
DISPLAY_TEXT = 'Slot Machine'
COLOR_BLACK = (255,255,255)
IMAGE_PATH = 'images\\'
IMG_EXT = '.png'
IMAGE_BG = 'bg' + IMG_EXT

#associative array for reel bet multipliers
REELS_X = (0,1,1,2,3,5,10)
NUM_REELS = 3

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
    #load image from file
    img = pygame.image.load(imgFile)
    
    #draw the image & update display
    screen.blit(img,dest)
    pygame.display.flip()

#draws the game screen
def drawGame(screen):
    #clear the screen & redraw bg
    screen.fill(COLOR_BLACK)
    drawImage(screen,IMAGE_PATH + IMAGE_BG)
    
# main game loop
def game(screen):
    while True: 
        
        #check all of the events that have occured since last loop
        for event in pygame.event.get():
            #if users quits, exit the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            #if the user clicks
            if event.type == MOUSEBUTTONUP:
                #get the mouse coordinates
                print event.pos
                #mX = event.pos()
                #mY\
            
        #redraw the screen & update display
        drawGame(screen)
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