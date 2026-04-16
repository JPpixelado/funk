# engine/input.py
import pygame

class InputHandler:
    def __init__(self):
        # Mapeamento de controles (pode ser alterado nas configurações futuramente)
        self.controls = {
            "note_left": [pygame.K_a, pygame.K_LEFT],
            "note_down": [pygame.K_s, pygame.K_DOWN],
            "note_up":   [pygame.K_w, pygame.K_UP],
            "note_right":[pygame.K_d, pygame.K_RIGHT],
            
            "ui_up":     [pygame.K_w, pygame.K_UP],
            "ui_down":   [pygame.K_s, pygame.K_DOWN],
            "ui_left":   [pygame.K_a, pygame.K_LEFT],
            "ui_right":  [pygame.K_d, pygame.K_RIGHT],
            
            "accept":    [pygame.K_RETURN, pygame.K_SPACE],
            "back":      [pygame.K_ESCAPE, pygame.K_BACKSPACE],
            "pause":     [pygame.K_RETURN, pygame.K_ESCAPE],
            
            "volume_up":   [pygame.K_EQUALS, pygame.K_PLUS],
            "volume_down": [pygame.K_MINUS],
            "volume_mute": [pygame.K_0],
            
            "freeplay_prev": [pygame.K_q],
            "freeplay_next": [pygame.K_e],
        }

        self.just_pressed = {}
        self.pressed = {}

    def update(self):
        """Atualiza o estado dos inputs"""
        keys = pygame.key.get_pressed()
        self.just_pressed.clear()
        
        for action, key_list in self.controls.items():
            pressed_now = any(keys[key] for key in key_list)
            
            if pressed_now and not self.pressed.get(action, False):
                self.just_pressed[action] = True
                
            self.pressed[action] = pressed_now

    def is_just_pressed(self, action: str) -> bool:
        return self.just_pressed.get(action, False)

    def is_pressed(self, action: str) -> bool:
        return self.pressed.get(action, False)