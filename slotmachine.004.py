import pygame, sys, random
from pygame.locals import *

#initialize pygame
pygame.init()

DISPLAY_SIZE = (600,386) #size of the screen (matches slot machine image)
DISPLAY_TEXT = 'Slot Machine' #window title
COLOR_BLACK = (255,255,255) #RGB for  black
IMG_PATH = 'images\\' #images folder path
IMG_EXT = '.png' #images extension

IMG_MCHN1 = 'machine1' + IMG_EXT #slot machine frame 1
IMG_MCHN2 = 'machine2' + IMG_EXT #slot machine frame 2

LVR_CURSOR = 'hand' + IMG_EXT

#possible game (lever) states
LVR_UP = 0
LVR_DOWN = 1

#possible game (lever) states and their images
LVR_STATES = {LVR_UP:IMG_MCHN1,
               LVR_DOWN:IMG_MCHN2}

LVR_RECT = (500,0) #lever area (x,y)

REELS_INIT = (0,0,0) #initial reels

#associative array for reel bet multipliers
REELS_MULTI = (0,1,1,2,3,5,10)

REELS_NUM = 3 #number of reels
REELS_Y=175 #reels y location on the screen
REELS_X=125 #first reels x location on the screen
REELS_XOFF=90 #x offset between each of the reels

REELS_RECT = list() #rectangles (x,y) for graphical location of reels

#calculates the rectangles (x,y) for each reel
for n in range(0,REELS_NUM):
    REELS_RECT.append((REELS_X+REELS_XOFF*n,REELS_Y))

#((REELS,175),(215,175),(305,175))

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

def drawReels(screen,reels):
    #for each spun reel
    for r in range(0,len(reels)):
        #get the img file for the reel
        imgFile = IMG_PATH + str(reels[r]) + IMG_EXT
        
        #draw the reel to the screen
        drawImage(screen,imgFile,REELS_RECT[r])
        
#draws an image
def drawImage(screen,imgFile,dest=(0,0)):
    #load image from file
    img = pygame.image.load(imgFile)
    
    #draw the image & update display
    screen.blit(img,dest)

#draws the game screen
def drawGame(screen,state,reels,msg=None):
    #clear the screen & redraw bg
    screen.fill(COLOR_BLACK)
    drawImage(screen,IMG_PATH + LVR_STATES[state])
    
    #redraw reels
    drawReels(screen,reels)
    pygame.display.flip()

# main game loop
def game(screen):
    state = LVR_UP #current game (lever) state
    reels = REELS_INIT #current reels
    msg = None # current message displayed on the screen
    
    while True: 
        #check all of the events that have occured since last loop
        for event in pygame.event.get():
            #if users quits, exit the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #REMOVED - FIX
            #elif event.type == MOUSEMOTION:
            #    #get the mouse coordinates
            #    mPos = event.pos
            #    
            #    if (mPos > LVR_RECT):
            #        pass
            #                       
            #if the user clicks down
            elif event.type == MOUSEBUTTONDOWN:
                #get the mouse coordinates
                mPos = event.pos
                
                #if the mouse position is within the lever area & lever is up
                if (mPos > LVR_RECT and state==LVR_UP):
                    #push down the lever & spin!
                    state=LVR_DOWN
                    reels=spin(REELS_NUM,len(REELS_MULTI))
            
            #if the user is letting up a click   
            elif event.type == MOUSEBUTTONUP:
                if(state==LVR_DOWN):
                    state=LVR_UP
            
        #redraw the screen & update display to the current game state
        drawGame(screen,state,reels,msg)

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