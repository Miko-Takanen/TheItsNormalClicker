#:The It's Normal Clicker- Made and Authored by AH6904 (Miko:T):#

#:IMPORTING--:
import pygame
import random
from shop import Shop
from button import Button
from playername import get_player_name
from pygame.locals import *
#--------------------------:

#:GET--------:
pygame.init()
window_surface = pygame.display.set_mode((800, 600))
player_name = get_player_name(window_surface)

with open("assets/clicker_count.txt", "a") as file:
    file.write(f"Player's Name: {player_name}\n")
    print(f"Player's Name: {player_name}")
#-----------------------------------------:

#:IMAGES----------------------------------------------------------------------:
normal_img = pygame.image.load("assets/images/btn_normal.png").convert_alpha()
hover_img = pygame.image.load("assets/images/btn_hover.png").convert_alpha()
down_img = pygame.image.load("assets/images/btn_down.png").convert_alpha()
#-------------------------------------------------------------------------:

#:CAPTIONS---:
sentences = [
     "Also try Cookie Clicker!", "Welcome!", 
     "Enjoy the clicking!", "It's Normal.", 
     "Those clicks are addicting.", "Listen to YonKaGor!", 
     "Betta Version.", "123. Would you agree that you're the only clicker?"
     ]
pygame.init()

random_sentence = random.choice(sentences)
title = (f"Hi {player_name}! | {random_sentence}")
pygame.display.set_caption(title)
#--------------------------------:

#:MUSIC FILES--:
music_files = [
"assets/audio/Music.mp3", 
"assets/audio/Music2.mp3", 
"assets/audio/Music3.wav",
"assets/audio/Music4.mp3",
]

pygame.init()
pygame.mixer.init()
#------------------:

#:COUNTER, FILING & AUDIO-----------------:
btn_rect = pygame.Rect(550, 400, 200, 168)
count = 0

def on_button_click():
    global count
    count += 1
    print(f"{player_name} clicked Routine_ball {count} times.")
    click_sound = pygame.mixer.Sound("assets/audio/click.mp3")
    click_sound.set_volume(1.0)
    click_sound.play()

    with open("assets/clicker_count.txt", "a") as file:
        file.write(f"Times {player_name} has clicked: {count}\n")

button = Button(
    images={'normal': normal_img, 'hover': hover_img, 'down': down_img},
    rect=btn_rect,
    callback=on_button_click)
#----------------------------:

#:BG COLORING-----------:
color1 = (165, 200, 230)
color2 = (255, 206, 27)
color3 = (255, 255, 0)
color4 = (0, 149, 228)

bg = pygame.Surface((800, 600))
bg.fill(color1)
pygame.draw.line(bg, color2, (0, 300), (800, 300), 50)
pygame.draw.line(bg, color2, (0, 350), (800, 350), 20)
#-----------------------------------------------------:

#:RESTART--------:
def reset_game(): 
    count = 0
    with open("assets/clicker_count.txt", "a") as file:
        file.write("Game has been reset.\n")
        
    return count
#---------------:

#:RUN & RENDER---:
is_running = True
music_playing = False
in_shop = False
current_music_index = 0

def render_text(surface, text, font_size, color, position):
            font = pygame.font.Font("assets/fonts/TCCEB.ttf", font_size)
            rendered_text = font.render(text, True, color)
            surface.blit(rendered_text, position)

while is_running: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e or event.type == pygame.QUIT:
            is_running = False       
            with open("assets/clicker_count.txt", "a") as file:
                file.write("Program has been closed.\n")
            print("Program Closed!")
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            count = reset_game()
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
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                if music_playing:
                    with open("assets/clicker_count.txt", "a") as file:
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
        window_surface.fill(color3)
        pygame.draw.line(window_surface, color4, (0, 300), (800, 300), 50)
        pygame.draw.line(window_surface, color4, (0, 350), (800, 350), 20)
        Shop.draw_shop(window_surface, count)
    
    else:
        window_surface.blit(bg, (0, 0))
        button.draw(window_surface)

        render_text(window_surface, f"Clicked: {count}", 36, (0, 120, 255), (5, 235))
        render_text(window_surface, "The It's Normal Clicker V1.5", 50, (0, 0, 0), (15, 34))
        render_text(window_surface, "The It's Normal Clicker V1.5", 50, (255, 255, 255), (13, 32))
        render_text(window_surface, "S = Go to Shop | R = Reset Count | N = Skip Song | E = Close", 25, (255, 206, 27), (5, 566))
            
    pygame.display.flip()
#------------------------: