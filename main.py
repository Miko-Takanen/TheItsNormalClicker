#:The It's Normal Clicker- Made and Authored by AH6904 (Miko:T):#

#:IMPORTING--:
import pygame
import random
from button import Button
#------------------------:

#:VARIABLES--:
pygame.init()
player_name = (input("Enter name:"))

#-----------------------------------:

#:CAPTIONS---------------------------------------------------------------------------------------------------------------------------------------------------------:
sentences = ["Also try Cookie Clicker!", "Welcome!", "Enjoy the clicking!", "It's Normal.", "Those clicks are addicting.", "Listen to YonKaGor!", "Betta Version."]
pygame.init()

random_sentence = random.choice(sentences)
title = (f"Hi {player_name}! | {random_sentence}")
pygame.display.set_caption(title)
#--------------------------------:

#:DP-SIZE & IMAGES----------------------------------:
window_surface = pygame.display.set_mode((800, 600))

normal_img = pygame.image.load("btn_normal.png").convert_alpha()
hover_img = pygame.image.load("btn_hover.png").convert_alpha()
down_img = pygame.image.load("btn_down.png").convert_alpha()
#-----------------------------------------------------------:

#add .ogg or .wav files and remove all "#" from all audio related code.
#:AUDIO FILES------:
#audio_files = [""] 
#pygame.init()
#pygame.mixer.init()


pygame.mixer.init()
pygame.mixer.music.load("Music.mp3")

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
#----------------------------------:

#:COUNTER, FILING & AUDIO-----------------:
btn_rect = pygame.Rect(550, 400, 200, 168)
count = 0
    
def on_button_click():
    global count
    count += 1
    print(f"{player_name} clicked Routine_ball {count} times.")
    
    #random_audio = random.choice(audio_files)
    #pygame.mixer.music.load(random_audio)
    #pygame.mixer.music.play() 
    
    with open("clicker_count.txt", "a") as file:
        file.write(f"Times {player_name} has clicked: {count}\n")
        
button = Button(
    images={'normal': normal_img, 'hover': hover_img, 'down': down_img},
    rect=btn_rect,
    callback=on_button_click)
#----------------------------:

#:BG COLORING-----------:
color1 = (165, 200, 230)
color2 = (255, 206, 27)

bg = pygame.Surface((800, 600))
bg.fill(color1)
pygame.draw.line(bg, color2, (0, 300), (800, 300), 50)
pygame.draw.line(bg, color2, (0, 350), (800, 350), 20)
#-----------------------------------------------------:

#:RESTART---------:
#def reset_game(): 
    #count = 0
    #return game_state


#game_state = reset_game()
#-------------------------:

#:RUN & RENDER---:
is_running = True

while is_running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False         
        button.handle_event(event)

    window_surface.blit(bg, (0, 0))
    button.draw(window_surface)

    font = pygame.font.Font("TCCEB.ttf", 36)
    text = font.render(f"Clicked: {count}", True, (0, 120, 255))
    window_surface.blit(text, (5, 235))

    font = pygame.font.Font("TCCEB.ttf", 50)
    text = font.render("The It's Normal Clicker V1.2", True, (255, 255, 255))
    window_surface.blit(text, (13, 32))
    text = font.render("The It's Normal Clicker V1.2", True, (255, 206, 27))
    window_surface.blit(text, (15, 30))
    
    pygame.display.flip()
#------------------------: