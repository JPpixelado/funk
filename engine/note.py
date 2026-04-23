# engine/note.py
import pygame
from engine.spritesheet import SpriteSheet

class Note:
    def __init__(self, time: float, direction: str, speed: float = 720):
        self.time = time
        self.direction = direction
        self.speed = speed
        self.hit = False
        self.miss = False
        self.alpha = 255

        self.x_positions = {"left": 308, "down": 382, "up": 456, "right": 530}
        self.x = self.x_positions[direction]
        self.y = -120

        self.spritesheet = None
        self.frame_index = 0

    def set_spritesheet(self, spritesheet: SpriteSheet):
        self.spritesheet = spritesheet

    def update(self, dt: float, song_position: float):
        if self.hit or self.miss:
            self.alpha = max(0, self.alpha - 1200 * dt)
            return

        spawn_ahead = 2000  # 2 segundos antes
        
        distance = ((self.time - spawn_ahead) - song_position) * (self.speed / 1000.0)
        self.y = 498 - distance
        self.frame_index = int(pygame.time.get_ticks() / 60) % 4

    def draw(self, surface):
        if not self.spritesheet:
            # fallback
            colors = {"left": (0, 255, 255), "down": (0, 255, 0),
                      "up": (255, 255, 0), "right": (255, 0, 255)}
            s = pygame.Surface((64, 64), pygame.SRCALPHA)
            pygame.draw.rect(s, colors[self.direction], (0, 0, 72, 72), border_radius=10)
            s.set_alpha(self.alpha)
            surface.blit(s, (self.x, self.y))
            return

        frame = self.spritesheet.get_frame(f"arrow{self.direction.capitalize()}")
        if frame:
            scaled = pygame.transform.scale(frame, (64, 64))
            scaled.set_alpha(self.alpha)
            surface.blit(scaled, (self.x, self.y))

        print(self.time, song_position, self.y)
        

    def should_remove(self, song_position: float) -> bool:
        return self.y > 800 or (self.time + 500 < song_position and not self.hit)