'''
Filename: slotmachine.py
Purpose:  A simple graphical slot machine game using PyGame
Author:   Ryan Blakely
Date Mod: June 7, 2013
Mod By:   Ryan Blakely

Git: https://github.com/Blakely/SlotMachine

Revision History:
    test.000.py - initial commit. draws game screen 
    test.001.py - gets random numbers & mouse event testing
    test.002.py - minor rev (last test). finished spin
    slotmachine.003.py - file rename, mouse events/lever animation
    slotmachine.004.py - draws reels, graphically-spins (no function)
    slotmachine.005.py - draws strings to screen. lots of code cleanup (basically functional)
    slotmachine.006.py - added game logic, calculations, game over. fully functional
     + sm_constants.py - moved constants here
    slotmachine.007.py - quit+reset button, code cleanup + comments
     + sm_constants.py - added button constants
     
(for full detailed revision history please see Git)
'''

#import needed modules + pygame
import pygame, sys, random
from pygame.locals import *

#import constants from slot machine constants file
from sm_constants import *

#initialize pygame
pygame.init()
pygame.font.init()

#====================================================================================
#                               DRAWING FUNCTIONS
#====================================================================================
        
#draws an image at a location on the pygame screen
# screen - the pygame screen being draw to
# imgFile - the image file to load to draw
# pos - the position (x,y) being drawn to, default 0,0
def drawImage(screen,imgFile,pos=(0,0)):
    #load image from file
    img = pygame.image.load(imgFile)
    
    #draw the image & update display
    screen.blit(img,pos)
    
#draws the reels to the screen
# screen - the pygame screen being drawn to
# reels - a list representing the spun reels
def drawReels(screen,reels):
    #for each spun reel
    for r in range(0,len(reels)):
        #get the img file for the reel
        imgFile = IMG_PATH + str(reels[r]) + IMG_EXT
        
        #draw the reel to the screen
        drawImage(screen,imgFile,REELS_POS[r])

#draws a string to the screen
# screen - the pygame screen being drawn to
# string - string being drawn to the screen
# size - size of the font to draw the screen in
# pos - position of the string on-screen (x,y)
def drawString(screen, string, size, pos):
    #create a font to draw with
    font = pygame.font.SysFont(FONT_TYPE, size)
    
    #create a font rendering and draw it to the screen
    label = font.render(string, 1, FONT_COLOR)
    screen.blit(label, pos)
    
#draw the game (UI) text to the screen
# screen - the pygame screen being drawn to
# texts - tuple of form (bet, pot, cash, msg), representing current game values
def drawGameText(screen,texts):
    
    #loop through all the possible game texts
    for t in range(0,len(GAME_TEXTS)):
        currText = GAME_TEXTS[t]
        
        #if the text is a lbl+value pair
        if ("txt" in currText):
            #draw the label
            drawString(screen,currText[TEXTS_TXT],currText[TEXTS_SIZE],currText[TEXTS_POS])
        
        #draw the value
        drawString(screen,str(texts[t]),currText[TEXTS_SIZE],currText[TEXTS_VPOS])

#draws the games buttons
# screen - the pygame screen being drawn to
# buttons - buttons to be drawn (dictionary - see BUTTONS constant)
def drawButtons(screen,buttons):
    #loop through each of the buttons to draw
    for btn in buttons.keys():
        #draw that button
        drawImage(screen,IMG_PATH + btn + IMG_EXT, buttons[btn])
        

#draws the game screen
# screen - the pygame screen being drawn to
# state - int representing the games current state
# reels - a list representing the spun reels
# texts - tuple of form (bet, pot, cash, msg), representing current game values
def drawGame(screen,state,reels,texts,buttons):
    #clear the screen & redraw bg
    screen.fill(COLOR_BLACK)
    drawImage(screen,IMG_PATH + LVR_STATES[state])
    
    drawReels(screen,reels) #redraw reels
    drawGameText(screen,texts) #redraw game text
    drawButtons(screen,buttons) #redraw the game buttons
    
    #update the display
    pygame.display.flip()

#======================================================================================
#                  GAME LOGIC/HANDLING FUNCTIONS
#======================================================================================

#gets a random number between 0 and maxNum
# maxNum - the maximum number allowed to be generated
#returns - random number
def getRandom(maxNum):
    return random.randint(0,maxNum-1)

#spins the reel
# numReels - number of reels to spin
# maxNum - the maximum "value" each reel can spin to (0 to maxNum)
#returns - list of integers representing the spun reels
def spin(numReels,maxNum):
    reels = list()
    
    #loop through all the required numbers
    for reel in range(0,numReels):
        reels.append(getRandom(maxNum))
    
    return reels;

#gets a value representing the state of the reels (nothing, matching, jackpot)
# reels - a list of integers representing the spun reels
#returns 0 if not matching
#        1 if matching
#        2 if jackpot
def checkReels(reels):
    reel = reels[0] #get the first reel value
    same = 1
    
    #loop through each reel
    for r in range(0,len(reels)):
        #if it does not match the before reel they are not the same & quit checking
        if (reels[r]!=reel):
            same=0
            break
    
    #if its the same and the jackpot reel, return jackpot
    if(same==1 and reel==JACKPOT):
        return 2;
    
    return same;

#process keyboard input to set bet
# bet - the current bet
# key - the keyboard key pressed
#returns - the new bet
def procBet(bet,key):
    betStr = str(bet) #get the bet string
                
    #try because chr will fail if character is > 255, but we dont care about them anyways
    try:
        #if the key is a backspace
        if key == K_BACKSPACE:
            betStr = betStr[0:-1] #remove the last digit
        
        #if key is a digit
        elif (chr(key).isdigit()):
            betStr += chr(key)  #add it to the bet string
        
        #if user entered an invalid bet (nothing)
        if(not betStr):
            return 0 #new bet of 0
    
    #if there was any problem, return the original bet
    except Exception:
        return bet
    
    #convert and return the new bet
    return int(betStr)

#process any buttons that may have been pressed
# buttons - buttons to check if pressed (dictionary - see BUTTONS constant)
# mPos - the mouse position (x,y)
#returns - string representing the clicked button (or None)
def procBtn(buttons,mPos):
    mX=mPos[0] #mouse x pos
    mY=mPos[1] #mouse y pos
    
    #loop through each of the buttons to check
    for btn in buttons.keys():
        top=(buttons[btn][0],buttons[btn][1]) #top left corner of click-able
        btm=(buttons[btn][2],buttons[btn][3]) #button right corner of clickable
        
        #if mouse click was in clickable area for button
        if (mX > top[0] and mY > top[1] and mX < btm[0] and mY < btm[1]):
            return btn #this button was clicked!
    
    #if no buttons were clicked, return None
    return None

#=========================================================================================
#                     MAIN/GAME FUNCTIONS
#=========================================================================================

#main game loop - runs until the user quits
# screen - 
def game(screen):
    #initial states for the game
    state = LVR_UP #current game (lever) state
    reels = REELS_INIT #current reels
    msg = MSG[TEXTS_INIT] # current message displayed on the screen
    bet = BET[TEXTS_INIT] #players current bet
    pot = POT[TEXTS_INIT] #current jackpot
    cash = CASH[TEXTS_INIT] #players current money
     
    #begin game loop
    while True:
        #check all of the events that have occured since last loop
        for event in pygame.event.get():
            #if users quits, exit the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == MOUSEBUTTONDOWN:
                #get the mouse coordinates & any button that may have been pressed
                mPos = event.pos
                btn = procBtn(BUTTONS,mPos)
                
                #if the user clicked the reset button 
                if (btn=="reset"):
                    #reset variables to their initial states
                    state = LVR_UP 
                    reels = REELS_INIT 
                    msg = MSG[TEXTS_INIT] 
                    bet = BET[TEXTS_INIT] 
                    pot = POT[TEXTS_INIT] 
                    cash = CASH[TEXTS_INIT]
                    
                #if the user clicked the quit button
                elif (btn=="quit"):
                    #exit the game
                    pygame.quit()
                    sys.exit()
                    
                #if the click position is within the lever area & lever is up
                elif (mPos > LVR_POS and state==LVR_UP):
                    
                    #perform necessary checks before spinning
                    #if the player doesnt have enough money...
                    if (bet>cash):
                        msg=MSG_CASH 
                    #if the player hasn't placed a valid bet...
                    elif (bet<=0):
                        msg=MSG_BET
                    #if the player is out of cash - game over!
                    elif (cash==0):
                        msg=MSG_ZERO
                
                    #otherwise, if were all good to go...
                    else:
                        #reset game message
                        msg=""
                        
                        #push down the lever & spin!
                        state=LVR_DOWN
                        reels=spin(REELS_NUM,len(REELS_MULTI))
                        
                        #check for a match on the spun reels
                        match=checkReels(reels)
                        winnings=0 #winnings holder variable
                        
                        #calculate moneys
                        cash=cash-bet
                        pot=pot+bet
                        
                        #if it was a win of some kind
                        if(match>0):
                            #add the bet multiplier to the winnings
                            winnings=bet*REELS_MULTI[reels[0]]
                            
                            msg = MSG_WIN + str(winnings)
                        
                        #if it was a jackpot win
                        if(match==2):
                            #clear out the jackpot
                            winnings += pot
                            pot=0
                            msg=MSG_JACKPOT
                        
                        #add winnings to cash
                        cash += winnings
                        
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
        drawGame(screen,state,reels,texts,BUTTONS)
    
    
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