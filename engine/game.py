# engine/game.py
import pygame
from engine.menu import MainMenu
from engine.freeplay import FreeplayMenu
from engine.levels import LevelSelect
from engine.settings import SettingsMenu
from engine.story import StoryMode

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.current_state = "main_menu"
        
        # Estados
        self.main_menu = MainMenu(self)
        self.freeplay = FreeplayMenu(self)
        self.level_select = LevelSelect(self)
        self.settings = SettingsMenu(self)
        self.story_mode = StoryMode(self)
        
        # Volume global (0.0 a 1.0)
        self.volume = 0.8
        pygame.mixer.music.set_volume(self.volume)

    def change_state(self, new_state: str):
        self.current_state = new_state

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Controle de volume global (sempre ativo)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                        self.volume = min(1.0, self.volume + 0.05)
                        pygame.mixer.music.set_volume(self.volume)
                    elif event.key == pygame.K_MINUS:
                        self.volume = max(0.0, self.volume - 0.05)
                        pygame.mixer.music.set_volume(self.volume)
                    elif event.key == pygame.K_0:
                        self.volume = 0.0
                        pygame.mixer.music.set_volume(0.0)

                # Passa evento para o estado atual
                if self.current_state == "main_menu":
                    self.main_menu.handle_event(event)
                elif self.current_state == "freeplay":
                    self.freeplay.handle_event(event)
                elif self.current_state == "level_select":
                    self.level_select.handle_event(event)
                elif self.current_state == "settings":
                    self.settings.handle_event(event)
                elif self.current_state == "story_mode":
                    self.settings.handle_event(event)

            # Update
            if self.current_state == "main_menu":
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
            
            if self.current_state == "main_menu":
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