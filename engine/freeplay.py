# engine/freeplay.py
import pygame
from engine.levels import LevelSelect

class FreeplayMenu:
    def __init__(self, game):
        self.game = game
        self.font_title = pygame.font.SysFont("Arial", 52, bold=True)
        self.font = pygame.font.SysFont("Arial", 36)
        
        self.options = ["Selecionar Fase", "Favoritos", "Voltar"]
        self.selected = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.select_option()

    def select_option(self):
        if self.options[self.selected] == "Selecionar Fase":
            self.game.change_state("level_select")
        elif self.options[self.selected] == "Voltar":
            self.game.change_state("main_menu")

    def update(self):
        pass

    def draw(self, surface):
        # Título
        title = self.font_title.render("FREEPLAY", True, (255, 220, 0))
        surface.blit(title, (640 - title.get_width()//2, 100))

        # Opções
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected else (140, 140, 140)
            text = self.font.render(option, True, color)
            surface.blit(text, (640 - text.get_width()//2, 280 + i * 70))