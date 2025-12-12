import pygame

#:CLASS------:
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
#--------------------------------------------------:


