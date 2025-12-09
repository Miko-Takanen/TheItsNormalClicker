import pygame

class Button:
    def __init__(self, images, rect, callback):
        self.images = images
        self.rect = rect
        self.callback = callback
        self.current_image = self.images['normal']
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.current_image = self.images['hover']
            else:
                self.current_image = self.images['normal']

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.current_image = self.images['down']
                self.callback()
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                self.current_image = self.images['hover']
            else:
                self.current_image = self.images['normal']
            
    def draw(self, surface):
        surface.blit(self.current_image, self.rect)


pygame.init()

pygame.display.set_caption('Listen to YonKaGor!')
window_surface = pygame.display.set_mode((800, 600))

normal_img = pygame.image.load("btn_normal.png").convert_alpha()
hover_img = pygame.image.load("btn_hover.png").convert_alpha()
down_img = pygame.image.load("btn_down.png").convert_alpha()

btn_rect = pygame.Rect(550, 360, 200, 168)

count = 0
    
def on_button_click():
    global count
    count += 1
    print(f"The player clicked Routine_ball {count} times")
     

button = Button(
    images={'normal': normal_img, 'hover': hover_img, 'down': down_img},
    rect=btn_rect,
    callback=on_button_click
)

bg = pygame.Surface((800, 600))
bg.fill((165, 200, 230))

is_running = True

while is_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        button.handle_event(event)


    window_surface.blit(bg, (0, 0))
    button.draw(window_surface)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Clicked: {count}", True, (0, 120, 255))
    window_surface.blit(text, (5, 300))

    font = pygame.font.Font(None, 50)
    text = font.render("The It's Normal Clicker V1.0", True, (255, 255, 255))
    window_surface.blit(text, (15, 30))

    pygame.display.update()