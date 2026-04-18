# engine/story.py
import pygame
import importlib

class StoryMode:
    def __init__(self, game):
        self.game = game
        self.font_title = pygame.font.SysFont("Arial", 52, bold=True)
        self.font = pygame.font.SysFont("Arial", 36)
        
        self.weeks = [
            {
                "name": "Week 1 - 2015",
                "levels": [
                    {"folder": "2015", "file": "2015", "difficulty": "Easy"}
                ]
            },
        ]
        self.selected_week = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected_week = (self.selected_week + 1) % len(self.weeks)
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.selected_week = (self.selected_week - 1) % len(self.weeks)
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.start_week()
            elif event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                print("🔙 ESC/BACKSPACE pressionado - Voltando ao menu...")
                self.game.change_state("main_menu")

    def start_week(self):
        week = self.weeks[self.selected_week]
        level = week["levels"][0]
        
        module_name = f"assets.{level['folder']}.{level['file']}"
        
        try:
            level_module = importlib.import_module(module_name)
            if hasattr(level_module, "play"):
                level_module.play(self.game)
            else:
                print(f"Erro: Função 'play()' não encontrada em {module_name}")
        except Exception as e:
            print(f"Erro ao carregar fase {level['folder']}: {e}")

    def update(self):
        pass

    def draw(self, surface):
        # Fundo escuro
        surface.fill((15, 15, 25))
        
        # Título
        title = self.font_title.render("MODO HISTÓRIA", True, (255, 220, 0))
        surface.blit(title, (640 - title.get_width() // 2, 100))

        # Semanas
        for i, week in enumerate(self.weeks):
            color = (255, 255, 100) if i == self.selected_week else (200, 200, 200)
            text = self.font.render(week["name"], True, color)
            surface.blit(text, (640 - text.get_width() // 2, 240 + i * 80))

        # Instrução de saída
        small_font = pygame.font.SysFont("Arial", 24)
        instr = small_font.render("ESC ou Backspace - Voltar ao Menu Principal", True, (140, 140, 140))
        surface.blit(instr, (640 - instr.get_width() // 2, 620))