import pygame
import sys
from time import time
import random
from pygame.locals import *
from pygame.compat import unichr_, unicode_


##Variables##

#Colors#
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

image = pygame.image.load ('cat.png')



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
                    degrees_to_rotate = random.randint (0,360) 
                    STATE = "Pair of objects"
                    print(STATE)
                    
            elif STATE == "Pair of objects":
                if event.type == KEYDOWN and event.key in KEYS.values():
                    #rotation and mirroring images
                    
                    time_when_reacted = time()
                    this_reaction_time = time_when_reacted - time_when_presented
                    this_correctness = (event.key == KEYS[image]) #YES/NO
                    STATE = "Feedback"
                    time_when_presented = time()
                    print(STATE)

            elif STATE == "Feedback":
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if trial_number < 20:
                        STATE = "Fixation"
                    else:
                        STATE = "Goodbye"
                    print(STATE)    
            
            if event.type == QUIT:
                STATE = "Quit" 
        
   #Automatic Transitions#
        
    if STATE == "Fixation": 
            if trial_number < 20:
                if (time() - time_when_presented) > 1:
                    STATE = "Pair of objects"
                    print (STATE)
            else: 
                STATE = "Goodbye"
                print (STATE)
        
        
    elif STATE == "Fixation":
            trial_number = trial_number + 1
            time_when_presented = time()
            STATE = "Pair of objects"
            print(STATE)
        
        
     # Drawing to the screen#
    if STATE == "Welcome":
            draw_welcome()
            draw_button(SCREEN_SIZE[0]*3/5, 450, "Press Space to continue", col_black)
            
            
    if STATE == "Instruction":
            draw_instruction()
            
    if STATE == "Fixation":
            draw_fixation()
        
    if STATE == "Pair of objects":
            draw_image1 ()
            draw_image2 ()
            draw_button(SCREEN_SIZE[0]*1/5, 450, "Yes", col_green)
            draw_button(SCREEN_SIZE[0]*4/5, 450, "No", col_red)
        
    if STATE == "Feedback":
            draw_feedback(this_correctness, this_reaction_time)
        
    if STATE == "Goodbye":
            draw_goodbye()
        
    if STATE == "Quit":
            pygame.quit()
            sys.exit()

    pygame.display.update()  
        
        
#Defining methods#
        
def draw_welcome ():
    text_surface = font.render("Mental Rotation Task", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Press Spacebar to continue", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,300)
    screen.blit(text_surface, text_rectangle)
    
def draw_instrcution (): #instructional text#
    text_surface = font.render("Instruction", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Two objects will be presented on the screen. They can be rotated or mirrored. Please choose if these objects are the same by pressing Y for yes or N for no.", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,200)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Press Spacebar to start experiment", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,300)
    screen.blit(text_surface, text_rectangle)
    
def draw_fixation(): #big cross in middle#
    text_surface = font_small.render("X", True, col_red, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,250)
    screen.blit(text_surface, text_rectangle)
    
def draw_button(xpos, ypos, label, color):
    text = font_small.render(label, True, color, BACKGR_COL)
    text_rectangle = text.get_rect()
    text_rectangle.center = (xpos, ypos)
    screen.blit(text, text_rectangle
    
def flip_image(image_path, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)
    rotated_image.show()
    
def rotate(image_path, degrees_to_rotate, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(saved_location)
    rotated_image.show()

def draw_image1(): #2 pictures being rotated#
    
        
    
def draw_image2():
    
       
def draw_feedback (this_correctness, this_reaction_time):
     if correct:
        text_surface = font_small.render("correct", True, col_black, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
        screen.blit(text_surface, text_rectangle)
        text_surface = font_small.render(str(int(reaction_time * 1000)) + "ms", True, col_black, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0,200)
        screen.blit(text_surface, text_rectangle)
    else:
        text_surface = font_small.render("Wrong key!", True, col_red, BACKGR_COL)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
        screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Press Spacebar to continue", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,300)
    screen.blit(text_surface, text_rectangle)
    
    
def draw_goodbye():
    text_surface = font_small.render("END OF THE EXPERIMENT", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,150)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Thank you for your participation!", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,200)
    screen.blit(text_surface, text_rectangle)
    text_surface = font_small.render("Close the application.", True, col_black, BACKGR_COL)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (SCREEN_SIZE[0]/2.0,250)
    screen.blit(text_surface, text_rectangle)
    

        
        
        
main()
        