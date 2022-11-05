import pygame
import time
import keyboard as kb

#class imports
import class_button as c_btn
import player as pl

pygame.init() # maek thing happn

  
SCREEN_HEIGHT = 540
SCREEN_WIDTH = 960

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

#game variables
start = False # for actually playing the game NOT for the app running


#Title and Icon
pygame.display.set_caption('Sleepy Dreamer')#Title
icon = pygame.image.load('icon.png')# load icon
pygame.display.set_icon(icon) #display icon

#set fps
clock = pygame.time.Clock()
FPS = 60

#define fonts
font = pygame.font.SysFont("arialblack", 40)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



#defien colours
WHITE = (255, 255, 255)
mainMenu_textcol = (200,200,100)




#load files
file_button_tex = pygame.image.load('assets/button.png').convert_alpha()



#player files
player_down = pygame.image.load('assets/player/player_dir-down.png')
player_up = pygame.image.load('assets/player/player_dir-up.png')
player_left = pygame.image.load('assets/player/player_dir-left.png')
player_right = pygame.image.load('assets/player/player_dir-right.png')


#instances
start_button = c_btn.Button(0, 0, file_button_tex, 10)




ply = pl.Player(270, 480, WHITE, 10, 10)



#Game Loop (gone sexual!) (GONE WRONG!)
running = True
while running:

    clock.tick(FPS)

    key = pygame.key.get_pressed()
    #gamestate shit
    if start_button.draw(screen):
        print(start)
        start = True
    #movement and stuff liek tht

    #rendering
    screen.fill((83,90,83))
    if start == True:
        ply.move()
        ply.draw(screen)
    draw_text("Test", font, mainMenu_textcol, 20, 40)
    start_button.draw(screen)


    #screen.blit(player_down, (100, 100))
    #event
    for event in pygame.event.get():

        #Quitting with X
        if event.type == pygame.QUIT:
            print("Game quit via X button")
            running = False
    pygame.display.update()
pygame.quit()