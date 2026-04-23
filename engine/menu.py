# engine/menu.py
import pygame

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.title_font = game.fonts.get("title")
        self.menu_font = game.fonts.get("menu")
        self.options = ["Modo História", "Freeplay", "Opções", "Créditos"]
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
        option = self.options[self.selected]
        if option == "Modo História":
            self.game.change_state("story_mode")
        elif option == "Freeplay":
            self.game.change_state("freeplay")
        elif option == "Opções":
            self.game.change_state("settings")

    def update(self):
        pass

    def draw(self, surface):
        title = self.title_font.render("FNFK", True, (255, 255, 255))
        surface.blit(title, (640 - title.get_width() // 2, 120))

        for i, option in enumerate(self.options):
            color = (255, 220, 0) if i == self.selected else (180, 180, 180)
            text = self.menu_font.render(option, True, color)
            surface.blit(text, (640 - text.get_width() // 2, 280 + i * 80))