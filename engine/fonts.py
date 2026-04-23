# engine/fonts.py
import pygame
import os

class GameFonts:
    def __init__(self):
        self.fonts = {}
        self.base_path = "assets/images/fonts"
        
        # Carrega as fontes principais
        self.load_font("title",    "font-full.ttf", 72)
        self.load_font("menu",     "font-full.ttf", 48)
        self.load_font("small",    "font.ttf", 32)
        self.load_font("score",    "font.ttf", 28)

    def load_font(self, name: str, filename: str, size: int):
        path = os.path.join(self.base_path, filename)
        try:
            self.fonts[name] = pygame.font.Font(path, size)
            print(f"✅ Fonte carregada: {name} ({size}px)")
        except Exception as e:
            print(f"❌ Erro ao carregar fonte {filename}: {e}")
            # Fallback para fonte do sistema
            self.fonts[name] = pygame.font.SysFont("Arial", size, bold=True)

    def get(self, name: str):
        return self.fonts.get(name)