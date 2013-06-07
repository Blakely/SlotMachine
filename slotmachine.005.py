import pygame, sys, random
from pygame.locals import *

#initialize pygame
pygame.init()
pygame.font.init()

DISPLAY_SIZE = (600,386) #size of the screen (matches slot machine image)
DISPLAY_TEXT = 'Slot Machine' #window title

#initial values
REELS_INIT = (0,0,0) #initial reels

#initial game-text parameters
#either of the form lbl+value, or just value
BET = {"init":1,
       "txt":"Current Bet:",
       "txtsize":25,
       "txtpos":(70,25),
       "valpos":(200,25)}

POT = {"init":0,
       "txt":"Current Jackpot:",
       "txtsize":18,
       "txtpos":(175,270),
       "valpos":(300,270)} 

CASH = {"init":100,
        "txt":"Your Money:",
        "txtsize":18,
        "txtpos":(150,360),
        "valpos":(250,360)}

MSG = {"init":"",
       "txtsize":18,
       "valpos":(360,170)}

GAME_TEXTS = (BET,POT,CASH,MSG)

COLOR_BLACK = (0,0,0) #RGB for black

FONT_COLOR = COLOR_BLACK #color of font
FONT_TYPE = 'Arial' #font family

MSG_ZERO = "Game Over."
MSG_CASH = "Not enough money!"
MSG_BET = "Please place a bet."

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

LVR_POS = (500,0) #lever area (x,y)

#associative array for reel bet multipliers
REELS_MULTI = (1,2,2,4,5,8,10)

REELS_NUM = 3 #number of reels
REELS_Y=175 #reels y location on the screen
REELS_X=125 #first reels x location on the screen
REELS_XOFF=90 #x offset between each of the reels

REELS_POS = list() #position (x,y) for graphical location of reels

#calculates the position (x,y) for each reel
for n in range(0,REELS_NUM):
    REELS_POS.append((REELS_X+REELS_XOFF*n,REELS_Y))

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
        drawImage(screen,imgFile,REELS_POS[r])
        
#draws an image
def drawImage(screen,imgFile,loc=(0,0)):
    #load image from file
    img = pygame.image.load(imgFile)
    
    #draw the image & update display
    screen.blit(img,loc)

def drawString(screen, string, size, loc):
    #create a font to draw with
    font = pygame.font.SysFont(FONT_TYPE, size)
    
    #create a font rendering and draw it to the screen
    label = font.render(string, 1, FONT_COLOR)
    screen.blit(label, loc)
    
#draw the game (UI) text to the screen
#texts - tuple of form (bet, pot, cash, msg)
def drawGameText(screen,texts):
    
    #loop through all the possible game texts
    for t in range(0,len(GAME_TEXTS)):
        currText = GAME_TEXTS[t]
        
        #if the text is a lbl+value pair
        if ("txt" in currText):
            #draw the label
            drawString(screen,currText["txt"],currText["txtsize"],currText["txtpos"])
        
        #draw the value
        drawString(screen,str(texts[t]),currText["txtsize"],currText["valpos"])


#draws the game screen
def drawGame(screen,state,reels,texts):
    #clear the screen & redraw bg
    screen.fill(COLOR_BLACK)
    drawImage(screen,IMG_PATH + LVR_STATES[state])
    
    #redraw reels
    drawReels(screen,reels)
    
    #redraw game text
    drawGameText(screen,texts)
    
    pygame.display.flip()


#process keyboard input to set bet
def procBet(bet,key):
    betStr = str(bet) #get the bet string
                
    #chr will fail if character is > 255, but we dont care about them anyways
    try:
        #if the key is a backspace
        if key == K_BACKSPACE:
            betStr = betStr[0:-1] #remove the last digit
        
        #if key is a digit
        elif (chr(key).isdigit()):
            betStr += chr(key)  #add it to the bet string
        
        #if user entered an invalid bet (0 or nothing)
        if(not betStr):
            return 0 #new bet of 1
    
    #if there was a problem, return the original bet
    except Exception:
        return bet
    
    #convert and return the new bet
    return int(betStr)

#check if there was a match & return the bet multiplier 
def getMultiplier(reels):
    reel = reels[0]
    same = True
    
    #loop through each reel
    for r in range(0,len(reels)):
        #if it does not match the before reel they are not the same & quit checking
        if (reels[r]!=reel):
            same=False 
            break
    
    #if all the reels are the same, return the multiplier
    if (same):
        return REELS_MULTI[reel]
    else: #otherwise return 0
        return 0

# main game loop
def game(screen):
    #initial states for the game
    state = LVR_UP #current game (lever) state
    reels = REELS_INIT #current reels
    msg = MSG["init"] # current message displayed on the screen
    bet = BET["init"] #players current bet
    pot = POT["init"] #current jackpot
    cash = CASH["init"] #players current money
    
    #begin game loop
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
            #    if (mPos > LVR_POS):
            #        pass
            #                       
            #if the user clicks down
            elif event.type == MOUSEBUTTONDOWN:
                #get the mouse coordinates
                mPos = event.pos
                
                #if the mouse position is within the lever area & lever is up & a bet is set
                if (mPos > LVR_POS and state==LVR_UP):
                    
                    #perform necessary checks before spinning
                    
                    #if the player is out of cash - game over!
                    if (cash==0):
                        msg=MSG_ZERO
                    #if the player doesnt have enough money...
                    if (bet>cash):
                        msg=MSG_CASH 
                    #if the player hasn't placed a valid bet...
                    elif (bet<=0):
                        msg=MSG_BET
                
                    #otherwise, if were all good to go...
                    else:
                        #push down the lever & spin!
                        state=LVR_DOWN
                        reels=spin(REELS_NUM,len(REELS_MULTI))
                        
                        #money calculations
                        cash=cash-bet
                        pot=pot+bet
                        cash=cash+betMulti()
                        
            #if the user is letting up a click   
            elif event.type == MOUSEBUTTONUP:
                if(state==LVR_DOWN):
                    state=LVR_UP
            
            #if the user is pressing a key
            elif event.type == KEYDOWN:
                #process the key and set the new bet
                bet=procBet(bet,event.key)
            
        #create tuple for game texts - must match format of GAME_TEXTS constant
        texts = (bet,pot,cash,msg)
        #redraw the screen & update display to the current game state
        drawGame(screen,state,reels,texts)

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