# engine/game.py
import pygame
import importlib
from engine.fonts import GameFonts
from engine.menu import MainMenu
from engine.freeplay import FreeplayMenu
from engine.levels import LevelSelect
from engine.settings import SettingsMenu
from engine.story import StoryMode
from engine.conductor import Conductor
from engine.chart import Chart


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.current_state = "main_menu"
        
        # Volume
        self.volume = 0.8
        pygame.mixer.music.set_volume(self.volume)

        # Fontes
        self.fonts = GameFonts()

        # Menus
        self.main_menu = MainMenu(self)
        self.freeplay = FreeplayMenu(self)
        self.level_select = LevelSelect(self)
        self.settings = SettingsMenu(self)
        self.story_mode = StoryMode(self)

        # Variáveis da fase
        self.conductor = Conductor()
        self.chart = None
        self.notes = []
        self.receptors = {}
        self.note_spritesheet = None
        self.receptor_spritesheet = None
        self.score = 0
        self.combo = 0

    def change_state(self, new_state: str):
        self.current_state = new_state

    # ===================== MÉTODO CHAMADO PELO STORY MODE =====================
    def start_story_level(self, chart_path: str, inst_path: str, folder: str, py_file: str = None):
        """Método mantido para compatibilidade com StoryMode"""
        if py_file:
            module_name = f"assets.{folder}.{py_file}"
            try:
                level_module = importlib.import_module(module_name)
                if hasattr(level_module, "play"):
                    level_module.play(self)   # ← Chama o play() da fase
                    return
            except Exception as e:
                print(f"⚠️ Erro ao executar {py_file}.py: {e}")

        # Fallback (caso não tenha .py)
        print(f"▶️ Carregando fase via JSON: {folder}")
        self.chart = Chart(chart_path)
        self.conductor.load_song(inst_path=inst_path, bpm=self.chart.bpm, offset=getattr(self.chart, 'offset', 0.0))
        self.notes = self.chart.generate_notes()
        self.receptors = {
            "left":  pygame.Rect(300, 500, 110, 110),
            "down":  pygame.Rect(420, 500, 110, 110),
            "up":    pygame.Rect(540, 500, 110, 110),
            "right": pygame.Rect(660, 500, 110, 110),
        }
        self.change_state("playing")
        self.conductor.play()

    # ===================== PLAYING STATE =====================
    def update_playing(self, dt):
        self.conductor.update(dt)
        
        for note in self.notes[:]:
            note.update(dt, self.conductor.song_position)
            if note.should_remove(self.conductor.song_position):
                self.notes.remove(note)

    def draw_playing(self):
        # Receptores
        if self.receptor_spritesheet:
            for direction, rect in self.receptors.items():
                frame = self.receptor_spritesheet.get_frame(f"arrow-{direction}-receptor")
                if frame:
                    scaled = pygame.transform.scale(frame, (140, 140))
                    self.screen.blit(scaled, (rect.x, rect.y))
                else:
                    pygame.draw.rect(self.screen, (80, 80, 100), rect, border_radius=15)
        else:
                pygame.draw.rect(self.screen, (80, 80, 100), rect, border_radius=15)

        # Notas
        for note in sorted(self.notes, key=lambda n: n.time):
            note.draw(self.screen)

        # HUD simples
        font = pygame.font.SysFont("Arial", 28)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (20, 20))

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Volume global
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_EQUALS, pygame.K_PLUS):
                        self.volume = min(1.0, self.volume + 0.05)
                        pygame.mixer.music.set_volume(self.volume)
                    elif event.key == pygame.K_MINUS:
                        self.volume = max(0.0, self.volume - 0.05)
                        pygame.mixer.music.set_volume(self.volume)
                    elif event.key == pygame.K_0:
                        self.volume = 0.0
                        pygame.mixer.music.set_volume(0.0)

                # Eventos
                if self.current_state == "main_menu":
                    self.main_menu.handle_event(event)
                elif self.current_state == "freeplay":
                    self.freeplay.handle_event(event)
                elif self.current_state == "level_select":
                    self.level_select.handle_event(event)
                elif self.current_state == "settings":
                    self.settings.handle_event(event)
                elif self.current_state == "story_mode":
                    self.story_mode.handle_event(event)

            # Update
            if self.current_state == "playing":
                self.update_playing(dt)
            elif self.current_state == "main_menu":
                self.main_menu.update()
            elif self.current_state == "freeplay":
                self.freeplay.update()
            elif self.current_state == "level_select":
                self.level_select.update()
            elif self.current_state == "settings":
                self.settings.update()
            elif self.current_state == "story_mode":
                self.story_mode.update()

            # Draw
            self.screen.fill((15, 15, 25))

            if self.current_state == "playing":
                self.draw_playing()
            elif self.current_state == "main_menu":
                self.main_menu.draw(self.screen)
            elif self.current_state == "freeplay":
                self.freeplay.draw(self.screen)
            elif self.current_state == "level_select":
                self.level_select.draw(self.screen)
            elif self.current_state == "settings":
                self.settings.draw(self.screen)
            elif self.current_state == "story_mode":
                self.story_mode.draw(self.screen)

            pygame.display.flip()