import pygame
import time
import keyboard as kb
import json
import os

#custom libraries
import class_button as c_btn
import player as pl
import sv_ld


pygame.init() # maek thing happn

  
SCREEN_HEIGHT = 540
SCREEN_WIDTH = 960

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

#game variables
start = False # for actually playing the game NOT for the app running
settings = False

#Title and Icon
pygame.display.set_caption('Sleepy Dreamer')#Title
icon = pygame.image.load('icon.png')# load icon
pygame.display.set_icon(icon) #display icon

#set fps
clock = pygame.time.Clock()
FPS = 60

#load files
file_button_tex = pygame.image.load('assets/button.png').convert_alpha()


#defien colours
WHITE = (255, 255, 255)
mainMenu_textcol = (200,200,100)

#player files
player_down = pygame.image.load('assets/player/player_dir-down.png')
player_up = pygame.image.load('assets/player/player_dir-up.png')
player_left = pygame.image.load('assets/player/player_dir-left.png')
player_right = pygame.image.load('assets/player/player_dir-right.png')

#instances
start_button = c_btn.Button(0, 130, file_button_tex, 10)
settings_button = c_btn.Button(0, 280, file_button_tex, 9)
quit_button = c_btn.Button(5, 420, file_button_tex, 6)
ply = pl.Player(270, 480, WHITE, 10, 10)

ply_pos = ply.rect.center
def save():
    print(ply_pos)
    sv_data = sv_ld.json_data
    sv_fileName = sv_ld.json_fileName
    sv_path = sv_ld.json_path
    sv_ld.save(sv_path, sv_fileName, sv_data, ply.health, ply.deaths, ply.slot0)



#define fonts
font = pygame.font.SysFont("arialblack", 40)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



#Game Loop (gone sexual!) (GONE WRONG!)
running = True
while running:
    ply_pos = ply.rect.center
    clock.tick(FPS)

    key = pygame.key.get_pressed()
    
    #gamestate shit
    if start_button.draw(screen):
        print("Start")
        start = True
    if settings_button.draw(screen):
        print("Settings")
        settings = True
    if quit_button.draw(screen):
        print("Quit")
        running = False
    #movement and stuff liek tht

    #rendering
    screen.fill((83,90,83))
    if start == True:
        save()
        ply.move()
        ply.draw(screen)
    start_button.draw(screen)
    settings_button.draw(screen)
    quit_button.draw(screen)
    draw_text("Title", font, mainMenu_textcol, 20, 40)
    draw_text("Play", font, mainMenu_textcol, 100, 190)
    draw_text("Settings", font, mainMenu_textcol, 50, 330)
    draw_text("Quit", font, mainMenu_textcol, 50, 440)
    #screen.blit(player_down, (100, 100))
    #event
    for event in pygame.event.get():

        #Quitting with X
        if event.type == pygame.QUIT:
            print("Game quit via X button")
            running = False
    pygame.display.update()
pygame.quit()
