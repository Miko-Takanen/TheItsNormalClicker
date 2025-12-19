import pygame

COLOR_SKY_BLUE = (165, 200, 230)
COLOR_YELLOW = (255, 206, 27)
COLOR_BRIGHT_YELLOW = (255, 255, 0)
COLOR_BLUE = (0, 149, 228)
COLOR_TEXT_BLUE = (0, 120, 255)


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def render_text(surface, text, font_size, color, position):
    font = pygame.font.Font("assets/fonts/TCCEB.ttf", font_size)
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, position)
