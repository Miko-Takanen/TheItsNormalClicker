import pygame
from utilities import render_text, COLOR_SKY_BLUE, COLOR_YELLOW, WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()

window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def get_player_name(window_surface):
    input_string = ""
    is_typing = True

    bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    bg.fill(COLOR_SKY_BLUE)
    pygame.draw.line(bg, COLOR_YELLOW, (0, 300), (WINDOW_WIDTH, 300), 50)
    pygame.draw.line(bg, COLOR_YELLOW, (0, 350), (WINDOW_WIDTH, 350), 20)

    while is_typing:
        window_surface.blit(bg, (0,0))
        render_text(window_surface, "The It's Normal Clicker V1.5", 50, (0, 0, 0), (15, 34))
        render_text(window_surface, "The It's Normal Clicker V1.5", 50, (255, 255, 255), (13, 32))
        render_text(window_surface, "Created by AH6904", 20, (0, 0, 0), (11, 80))
        render_text(window_surface, "Created by AH6904", 20, (255, 255, 255), (10, 78))
        render_text(window_surface, "@KisuRepo 2025", 20, (0, 0, 0), (662, 575))
        render_text(window_surface, "Enter name to start:", 36, (0, 120, 255), (50, 240))
        render_text(window_surface, input_string, 36, (0, 120, 255), (325, 240))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_typing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_typing = False
                elif event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                else:
                    input_string += event.unicode

        pygame.display.flip()
    
    return input_string

def render_text(surface, text, font_size, color, position):
    font = pygame.font.Font("assets/fonts/TCCEB.ttf", font_size)
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, position)

pygame.display.flip()
