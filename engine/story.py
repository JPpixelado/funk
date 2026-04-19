# engine/story.py
import pygame
import os

class StoryMode:
    def __init__(self, game):
        self.game = game
        self.font_title = self.game.fonts.get("title")
        self.font_menu = self.game.fonts.get("menu")
        self.font_small = self.game.fonts.get("small")

        self.weeks = []
        assets_dir = "assets"

        print("🔍 Detectando fases em 'assets/'...")

        for folder in os.listdir(assets_dir):
            folder_path = os.path.join(assets_dir, folder)
            if not os.path.isdir(folder_path):
                continue

            icon_path = os.path.join(folder_path, "icon.png")
            if not os.path.exists(icon_path):
                continue

            try:
                icon_surf = pygame.image.load(icon_path).convert_alpha()
            except:
                icon_surf = None

            # Detecta arquivo .py
            py_file = None
            for file in os.listdir(folder_path):
                if file.endswith(".py") and not file.startswith("__"):
                    py_file = file[:-3]
                    break

            # Detecta dificuldades
            difficulties = {}
            for diff, suffix in [("easy", "-easy"), ("normal", ""), ("hard", "-hard")]:
                json_name = f"{folder}{suffix}.json"
                json_path = os.path.join(folder_path, json_name)
                if os.path.exists(json_path):
                    difficulties[diff] = json_name

            if difficulties:
                self.weeks.append({
                    "name": folder.replace("_", " ").title(),
                    "folder": folder,
                    "icon_surf": icon_surf,
                    "py_file": py_file,
                    "difficulties": difficulties
                })
                print(f"✅ Fase detectada: {folder}")

        self.weeks.sort(key=lambda w: w["name"])

        # Proteção contra lista vazia
        self.selected_week = 0
        self.selected_diff = 0

        if not self.weeks:
            print("⚠️  Nenhuma fase encontrada! Coloque pastas com 'icon.png' em assets/")

        # Ícones de dificuldade
        self.diff_icons = {}
        for diff in ["easy", "normal", "hard"]:
            path = f"assets/images/{diff}.png"
            if os.path.exists(path):
                try:
                    self.diff_icons[diff] = pygame.image.load(path).convert_alpha()
                except:
                    pass

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if not self.weeks:
            if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                self.game.change_state("main_menu")
            return

        if event.key in (pygame.K_DOWN, pygame.K_s):
            self.selected_week = (self.selected_week + 1) % len(self.weeks)
            self.selected_diff = 0
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.selected_week = (self.selected_week - 1) % len(self.weeks)
            self.selected_diff = 0
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            available = list(self.weeks[self.selected_week]["difficulties"].keys())
            self.selected_diff = (self.selected_diff + 1) % len(available)
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            available = list(self.weeks[self.selected_week]["difficulties"].keys())
            self.selected_diff = (self.selected_diff - 1) % len(available)
        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.start_selected_level()
        elif event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
            print("🔙 Voltando ao menu principal...")
            self.game.change_state("main_menu")

    def start_selected_level(self):
        if not self.weeks:
            return
        week = self.weeks[self.selected_week]
        available_diffs = list(week["difficulties"].keys())
        diff = available_diffs[self.selected_diff]
        json_filename = week["difficulties"][diff]

        chart_path = f"assets/{week['folder']}/{json_filename}"
        inst_path = f"assets/{week['folder']}/inst.ogg"

        self.game.start_story_level(
            chart_path=chart_path,
            inst_path=inst_path,
            folder=week["folder"],
            py_file=week["py_file"]
        )

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((15, 15, 25))

        title = self.font_title.render("MODO HISTÓRIA", True, (255, 220, 0))
        surface.blit(title, (640 - title.get_width() // 2, 60))

        if not self.weeks:
            font = pygame.font.SysFont("Arial", 36)
            text = font.render("Nenhuma fase encontrada", True, (255, 100, 100))
            surface.blit(text, (640 - text.get_width() // 2, 300))
            text2 = font.render("Coloque pastas com icon.png em assets/", True, (180, 180, 180))
            surface.blit(text2, (640 - text2.get_width() // 2, 360))
            return

        # Lista de semanas
        for i, week in enumerate(self.weeks):
            color = (255, 255, 100) if i == self.selected_week else (200, 200, 200)
            text = self.font_menu.render(week["name"], True, color)
            y = 180 + i * 70
            surface.blit(text, (80, y))

            if week["icon_surf"]:
                small_icon = pygame.transform.scale(week["icon_surf"], (64, 64))
                surface.blit(small_icon, (380, y - 8))

        # Ícone grande
        current = self.weeks[self.selected_week]
        if current["icon_surf"]:
            big_icon = pygame.transform.scale(current["icon_surf"], (280, 280))
            surface.blit(big_icon, (720, 160))

        # Dificuldades
        available = list(current["difficulties"].keys())
        start_x = 640 - (len(available) * 110) // 2

        for i, diff in enumerate(available):
            x = start_x + i * 110
            icon = self.diff_icons.get(diff)
            if icon:
                surface.blit(pygame.transform.scale(icon, (80, 80)), (x, 480))

            color = (255, 255, 255) if i == self.selected_diff else (140, 140, 140)
            text = self.font_small.render(diff.upper(), True, color)
            surface.blit(text, (x + 40 - text.get_width() // 2, 580))

        # Instrução
        instr = pygame.font.SysFont("Arial", 22).render(
            "ESC ou Backspace - Voltar ao Menu", True, (140, 140, 140))
        surface.blit(instr, (640 - instr.get_width() // 2, 660))