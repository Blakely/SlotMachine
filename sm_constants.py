#=======================================================================================
#                      CONSTANTS
#=======================================================================================

DISPLAY_SIZE = (600,386) #size of the screen (matches slot machine image)
DISPLAY_TEXT = 'Slot Machine' #window title

#initial values
REELS_INIT = (0,0,0) #initial reels

#dimensions of the games buttons
BTN_WIDTH=80
BTN_HEIGHT=40
#draw start position for the games buttons (one on top of the other)
BTN_X=5
BTN_Y=120
#"rectangles" representing the games buttons
# -- they will be right ontop of eachother
BTNRESET_RECT = (BTN_X,BTN_Y,BTN_X+BTN_WIDTH,BTN_Y+BTN_HEIGHT)
BTNQUIT_RECT = (BTN_X,BTN_Y+BTN_HEIGHT,BTN_X+BTN_WIDTH,BTN_Y+BTN_HEIGHT+BTN_HEIGHT)

#button identifiers
BTNRESET="reset"
BTNQUIT="quit"

#the games buttons
BUTTONS = {BTNRESET:BTNRESET_RECT,
           BTNQUIT:BTNQUIT_RECT}

#dictionary-key names for the GAME_TEXT dictionary
TEXTS_INIT="init"
TEXTS_TXT="txt"
TEXTS_SIZE="txtsize"
TEXTS_POS="txtpos"
TEXTS_VPOS="valpos"

#initial game-text parameters
#either of the form lbl+value, or just value
BET = {TEXTS_INIT:1,
       TEXTS_TXT:"Bet ($):",
       TEXTS_SIZE:26,
       TEXTS_POS:(100,25),
       TEXTS_VPOS:(190,25)}

POT = {TEXTS_INIT:0,
       TEXTS_TXT:"Jackpot ($):",
       TEXTS_SIZE:18,
       TEXTS_POS:(180,270),
       TEXTS_VPOS:(275,270)} 

CASH = {TEXTS_INIT:100,
        TEXTS_TXT:"Your Money ($):",
        TEXTS_SIZE:18,
        TEXTS_POS:(140,357),
        TEXTS_VPOS:(270,357)}

MSG = {TEXTS_INIT:"Click the lever!",
       TEXTS_SIZE:25,
       TEXTS_VPOS:(180,125)}

GAME_TEXTS = (BET,POT,CASH,MSG)

COLOR_BLACK = (0,0,0) #RGB for black

FONT_COLOR = COLOR_BLACK #color of font
FONT_TYPE = 'Arial' #font family

#various strings used in game messages
MSG_ZERO = "Game Over."
MSG_CASH = "Not enough money!"
MSG_BET = "Please place a bet."
MSG_JACKPOT = "JACKPOT!"
MSG_WIN = "You win $"

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
REELS_MULTI = (2,2,3,5,6,10,10)

JACKPOT = len(REELS_MULTI) #jackpot reel

REELS_NUM = 3 #number of reels
REELS_Y=175 #reels y location on the screen
REELS_X=125 #first reels x location on the screen
REELS_XOFF=90 #x offset between each of the reels

REELS_POS = list() #position (x,y) for graphical location of reels

#calculates the position (x,y) for each reel
for n in range(0,REELS_NUM):
    REELS_POS.append((REELS_X+REELS_XOFF*n,REELS_Y))