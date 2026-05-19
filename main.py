#:The It's Normal Clicker- Made and Authored by AH6904 (Miko:T):#

#:IMPORTING--:
import pygame
import random
from shop import Shop
from button import Button
from playername import get_player_name
from pygame.locals import *
from utilities import *
from constants import * 
#--------------------------:

#:GET--------:
pygame.init()
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
bg.fill(COLOR_SKY_BLUE)
pygame.draw.line(bg, COLOR_YELLOW, (0, 300), (WINDOW_WIDTH, 300), 50)
pygame.draw.line(bg, COLOR_YELLOW, (0, 350), (WINDOW_WIDTH, 350), 20)

player_name = get_player_name(window_surface)

with open(CLICKER_COUNT_FILE, "a") as file:
    file.write(f"Player's Name: {player_name}\n")
    print(f"Player's Name: {player_name}")
#-----------------------------------------:

#:IMAGES------------------------------------------------------:
normal_img = pygame.image.load(IMG_BTN_NORMAL).convert_alpha()
hover_img = pygame.image.load(IMG_BTN_HOVER).convert_alpha()
down_img = pygame.image.load(IMG_BTN_DOWN).convert_alpha()
#---------------------------------------------------------:

#:CAPTIONS---:
pygame.init()
random_sentence = random.choice(CAPTION_SENTENCES)
title = f"Hi {player_name}! | {random_sentence}"
pygame.display.set_caption(title)
#--------------------------------:

#:MUSIC FILES------------:
music_files = MUSIC_FILES
pygame.mixer.init()
#------------------:

#:COUNTER, FILING & AUDIO-----------------:
btn_rect = pygame.Rect(550, 400, 200, 168)
count = 0

def on_button_click():
    global count
    count += 1
    print(f"{player_name} clicked Routine_ball {count} times.")
    click_sound = pygame.mixer.Sound(CLICK_SOUND)
    click_sound.set_volume(1.0)
    click_sound.play()

def save_click_count():
    with open(CLICKER_COUNT_FILE, "a") as file:
        file.write(f"Times {player_name} has clicked: {count}\n")
    print(f"Saved click count: {count}")

button = Button(
    images={'normal': normal_img, 'hover': hover_img, 'down': down_img},
    rect=btn_rect,
    callback=on_button_click)
#----------------------------:

#:RESTART--------:
def reset_game(): 
    global count
    count = 0
    with open(CLICKER_COUNT_FILE, "a") as file:
        file.write("Game has been reset.\n")
    return count
#---------------:

#:RUN & RENDER---:
is_running = True
music_playing = False
in_shop = False
current_music_index = 0

while is_running: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e or event.type == pygame.QUIT:
            save_click_count()
            is_running = False       
            with open(CLICKER_COUNT_FILE, "a") as file:
                file.write("Program has been closed.\n")
            print("Program Closed!")
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()
            print("Game Reset!")  
        
        if in_shop:
            pygame.mixer.music.set_volume(0.1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                in_shop = False
                pygame.mixer.music.set_volume(0.3)
        else:
            button.handle_event(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                in_shop = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n and music_playing:
            with open(CLICKER_COUNT_FILE, "a") as file:
                file.write("Song has been skipped.\n")
            print("Song Skipped!")
            current_music_index = (current_music_index + 1) % len(music_files)
            pygame.mixer.music.load(music_files[current_music_index])
            pygame.mixer.music.play(1)
    
    if not music_playing:
        pygame.mixer.music.load(music_files[current_music_index])
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.3)
        music_playing = True
    
    if not pygame.mixer.music.get_busy():
        music_playing = False
        current_music_index = random.randint(0, len(music_files) -1)
        pygame.mixer.music.load(music_files[current_music_index])
        pygame.mixer.music.play(1)
    
    if in_shop:
        window_surface.fill(COLOR_BRIGHT_YELLOW)
        pygame.draw.line(window_surface, COLOR_BLUE, (0, 300), (WINDOW_WIDTH, 300), 50)
        pygame.draw.line(window_surface, COLOR_BLUE, (0, 350), (WINDOW_WIDTH, 350), 20)
        Shop.draw_shop(window_surface, count)
    
    else:
        window_surface.blit(bg, (0, 0))
        button.draw(window_surface)

        render_text(window_surface, f"Clicked: {count}", 36, COLOR_TEXT_BLUE, (5, 235))
        render_text(window_surface, "The It's Normal Clicker V1.5", 50, (0, 0, 0), (15, 34))
        render_text(window_surface, "The It's Normal Clicker V1.5", 50, (255, 255, 255), (13, 32))
        render_text(window_surface, "S = Go to Shop | R = Reset Count | N = Skip Song | E = Close", 25, COLOR_YELLOW, (5, 566))
            
    pygame.display.flip()
#------------------------:
