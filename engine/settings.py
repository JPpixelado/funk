# engine/settings.py
import pygame

class SettingsMenu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("Arial", 36)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                self.game.change_state("main_menu")

    def update(self):
        pass

    def draw(self, surface):
        text = self.font.render("Configurações - Em desenvolvimento", True, (255, 255, 255))
        surface.blit(text, (400, 300))