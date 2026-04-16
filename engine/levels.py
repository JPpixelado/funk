# engine/levels.py
import pygame
import importlib
import os

class LevelSelect:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont("Arial", 38)
        self.small_font = pygame.font.SysFont("Arial", 28)
        
        # Lista de fases (pode ser carregada de uma pasta futuramente)
        self.levels = [
            {"name": "2015", "folder": "2015", "file": "2015", "difficulty": "Easy"},
            # Adicione mais fases aqui
        ]
        self.selected = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected = (self.selected + 1) % len(self.levels)
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.selected = (self.selected - 1) % len(self.levels)
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.start_level()
            elif event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                self.game.change_state("freeplay")

    def start_level(self):
        level = self.levels[self.selected]
        folder = level["folder"]
        module_name = f"assets.{folder}.{level['file']}"
        
        try:
            level_module = importlib.import_module(module_name)
            # Chama função play() do arquivo da fase
            if hasattr(level_module, "play"):
                level_module.play(self.game)
            else:
                print(f"Erro: Função 'play()' não encontrada em {module_name}")
        except Exception as e:
            print(f"Erro ao carregar fase {level['name']}: {e}")

    def update(self):
        pass

    def draw(self, surface):
        title = self.font.render("SELECIONAR FASE", True, (255, 220, 0))
        surface.blit(title, (640 - title.get_width()//2, 80))

        for i, level in enumerate(self.levels):
            color = (255, 255, 100) if i == self.selected else (200, 200, 200)
            text = self.font.render(level["name"], True, color)
            surface.blit(text, (640 - text.get_width()//2, 200 + i * 70))
            
            diff = self.small_font.render(level["difficulty"], True, (100, 200, 255))
            surface.blit(diff, (750, 205 + i * 70))