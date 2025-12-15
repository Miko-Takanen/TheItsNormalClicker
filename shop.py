import pygame

shop_items = {
    "Click Boost": {"cost": 10, "effect": "Increase clicks by 2"}, 
    "Auto Clicker": {"cost": 50, "effect": "Adds 1 click per second"},
}

def open_shop(window_surface, count):
    shop_running = True

    while shop_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shop_running = False

        window_surface.fill((169, 169, 169))
        draw_shop(window_surface, count)
        pygame.display.flip()
        
def draw_shop(window_surface, count):
    font = pygame.font.Font("assets/fonts/TCCBE.ttf", 36)
    y_offset = 20

    for item, details in shop_items.items():
        text = f"{item}: Cost {details['cost']}, Effect: {details['effect']}"
        label = font.render(text, True, (0, 0, 0))
        window_surface.blit(label, (30, y_offset))
        y_offset += 40

    y_offset += 30
    click_label = font.render(f"Your Clicks: {count}", True, (0, 120, 225))
    window_surface.blit(click_label, (30, y_offset))
    
    text = font.render("ESC = Back", True, (255, 206, 27))
    window_surface.blit(text, (15, 560))
        