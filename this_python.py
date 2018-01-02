import pygame
import sys
from time import time
import random
from pygame.locals import *
from pygame.compat import unichr_, unicode_

##Variables#

# Colors
col_white = (250, 250, 250)
col_black = (0, 0, 0)
col_grey = (220, 220, 220)
col_red = (250, 0, 0)
col_green = (0, 200, 0)
col_blue = (0, 0, 250)
col_yellow = (250,250,0)

KEYS = {"Yes": K_y,
        "No": K_n}

BACKGR_COL = col_grey
SCREEN_SIZE = (700, 500)

pygame.init()
pygame.display.set_mode(SCREEN_SIZE) 
pygame.display.set_caption("Mental Rotation Task")

screen = pygame.display.get_surface()
screen.fill(BACKGR_COL)

font = pygame.font.Font(None, 80)
font_small = pygame.font.Font(None, 40) 


##METHOD##

def main ():
    
    STATE = "Welcome"
    
    trial_number = 0
    
    while True:
        pygame.display.get_surface().fill(BACKGR_COL)
        
   #Transitions#
       for event in pygame.event.get():                        
            if STATE == "Welcome":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    STATE = "Instruction"
                    print(STATE)
                    
            if STATE == "Instruction":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    STATE = "Fixation"
                    print(STATE)
                    
            if STATE == "Fixation":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    STATE = "Pair of objects"
                    print(STATE)
                    
            elif STATE == "Pair of objects":
                if event.type == KEYDOWN and event.key in KEYS.values():
                    time_when_reacted = time()
                    this_reaction_time = time_when_reacted - time_when_presented
                    this_correctness = (event.key == KEYS[this_color]) #YES/NO
                    STATE = "Feedback"
                    time_when_presented = time()
                    print(STATE)

            elif STATE == "Feedback":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if trial_number < 20:
                        STATE = "Fixation"
                    else:
                        STATE = "goodbye"
                    print(STATE)    
            
            if event.type == QUIT:
                STATE = "quit" 
        
        #Automatic Transitions#
        
        if STATE == "Fixation": 
            if trial_number < 20:
                if (time() - time_when_presented) > 1:
                    STATE = "Pair of objects"
                    print (STATE)
            else: 
                STATE = "goodbye"
                print (STATE)
        
        
        elif STATE == "Fixation":
            trial_number = trial_number + 1
            this_word  = pick_color() #pick object#
            this_color = pick_color() #pick object#
            time_when_presented = time()
            STATE = "Pair of objects"
            print(STATE)
        
        
      # Drawing to the screen  Change to our States
        if STATE == "welcome":
            draw_welcome()
            draw_button(SCREEN_SIZE[0]*1/5, 450, "Red: X", col_red)
            draw_button(SCREEN_SIZE[0]*3/5, 450, "Green: N", col_green)
            draw_button(SCREEN_SIZE[0]*4/5, 450, "Blue: M", col_blue)
        
        if STATE == "wait_for_response":
            draw_stimulus(this_color, this_word)
            draw_button(SCREEN_SIZE[0]*1/5, 450, "Red: X", col_red)
            draw_button(SCREEN_SIZE[0]*3/5, 450, "Green: N", col_green)
            draw_button(SCREEN_SIZE[0]*4/5, 450, "Blue: M", col_blue)
        
        if STATE == "feedback":
            draw_feedback(this_correctness, this_reaction_time)
        
        if STATE == "goodbye":
            draw_goodbye()
        
        if STATE == "quit":
            pygame.quit()
            sys.exit()

        pygame.display.update()  
        