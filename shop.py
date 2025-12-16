import pygame

button_rect = None

shop_buff = { 
    "Auto Clicker": {"cost": 50, "effect": "Adds 1 click per second"},
}

def open_shop(window_surface, count):
    shop_running = True

    while shop_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shop_running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button_rect.collidepoint(mouse_pos):
                        if count >= shop_buff["Auto Clicker"]["cost"]:
                            count -= shop_buff["Auto Clicker"]["cost"]
                            click_rate += 1
        
def draw_shop(window_surface, count):
    font = pygame.font.Font("assets/fonts/TCCBE.ttf", 36)
    y_offset = 20

    for item, details in shop_buff.items():
        text = f"{item}: Cost {details['cost']}, Effect: {details['effect']}"
        label = font.render(text, True, (0, 0, 0))
        window_surface.blit(label, (30, y_offset))
        y_offset += 40
    
    global button_rect
    button_rect = pygame.Rect(30, y_offset + 50, 150, 40)
    
    click_label = font.render(f"Your Clicks: {count}", True, (0, 120, 225))
    pygame.draw.rect(window_surface, (0, 200, 0), button_rect)
    window_surface.blit(click_label, (30, y_offset))

    text = font.render("ESC = Back", True, (255, 206, 27))
    window_surface.blit(text, (15, 560))
    
    pygame.display.flip()