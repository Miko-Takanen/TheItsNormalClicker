import pygame
from button import Shop_Button


shop_buff = { 
    "Auto Clicker": {"cost": 50, "effect": "Adds 1 click per second"},
}
class Shop():
    def open_shop(window_surface, count):
        shop_running = True

        while shop_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    shop_running = False
        
    def draw_shop(window_surface, count):
        font = pygame.font.Font("assets/fonts/TCCBE.ttf", 36)
        y_offset = 20

        for item, details in shop_buff.items():
            text = f"{item}: Cost {details['cost']}, Effect: {details['effect']}"
            label = font.render(text, True, (0, 0, 0))
            window_surface.blit(label, (30, y_offset))
            y_offset += 40

            buff = Buff(window_surface, count)     
        text = font.render("ESC = Back", True, (255, 206, 27))
        window_surface.blit(text, (15, 560))

        pygame.display.flip()

class Buff():
    def __init__(self, window_surface, count):
        font = pygame.font.Font("assets/fonts/TCCBE.ttf", 36)
        y_offset = 60
        global button_rect
        button_rect = pygame.Rect(30, y_offset + 50, 150, 40)
        pygame.draw.rect(window_surface, (0, 200, 0), button_rect)
    
        click_label = font.render(f"Your Clicks: {count}", True, (0, 120, 225))
        pygame.draw.rect(window_surface, (0, 200, 0), button_rect)
        window_surface.blit(click_label, (30, 60))
    