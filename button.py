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
        surface.blit(self.current_image, self.rect.topleft)

class Shop_Button:
    def __init__(self, button, rect1, callback1):
        self.button = button
        self.rect = rect1
        self.callback = callback1

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
#--------------------------------------------------:


