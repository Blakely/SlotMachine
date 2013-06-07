import pygame, sys, random
from pygame.locals import *

#initialize pygame
pygame.init()

DISPLAY_SIZE = (600,386)
DISPLAY_TEXT = 'Slot Machine'
COLOR_BLACK = (255,255,255)
IMG_PATH = 'images\\'
IMG_EXT = '.png'

IMG_MCHN1 = 'machine1' + IMG_EXT
IMG_MCHN2 = 'machine2' + IMG_EXT

LVR_CURSOR = 'hand' + IMG_EXT

LVR_UP = 0
LVR_DOWN = 1

GAME_STATES = {LVR_UP:IMG_MCHN1,
               LVR_DOWN:IMG_MCHN2}

LVR_RECT = (500,0)

#associative array for reel bet multipliers
REELS_X = (0,1,1,2,3,5,10)
NUM_REELS = 3

#gets a random number
def getRandom(maxNum):
    return random.randint(0,maxNum-1)

#spins the reel (returns random numbers)
def getReels(numReels,maxNum):
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
def drawGame(screen,stateImg):
    #clear the screen & redraw bg
    screen.fill(COLOR_BLACK)
    drawImage(screen,IMG_PATH + stateImg)

def drawLvrCursor(screen):
    


# main game loop
def game(screen):
    state = LVR_UP;
    
    while True: 
        
        #check all of the events that have occured since last loop
        for event in pygame.event.get():
            #if users quits, exit the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            #if the mouse has been moved
            elif event.type == MOUSEMOTION:
                #get the mouse coordinates
                mPos = event.pos
                
                if (mPos > LVR_RECT):
                    cursor = 
                
            #if the user clicks down
            elif event.type == MOUSEBUTTONDOWN:
                #get the mouse coordinates
                mPos = event.pos
                
                #if the mouse position is within the lever area & lever is up
                if (mPos > LVR_RECT and state==LVR_UP):
                    #push down the lever & spin!
                    state=LVR_DOWN
                    #spin!
            
            #if the user is letting up a click   
            elif event.type == MOUSEBUTTONUP:
                if(state==LVR_DOWN):
                    state=LVR_UP
            
        #redraw the screen & update display to the current game state
        drawGame(screen,GAME_STATES[state])
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