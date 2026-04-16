# engine/note.py
import pygame
from engine.spritesheet import SpriteSheet

class Note:
    def __init__(self, time: float, direction: str, speed: float = 720):
        self.time = time                    # ms
        self.direction = direction          # "left", "down", "up", "right"
        self.speed = speed
        self.hit = False
        self.miss = False
        self.alpha = 255

        # Posição inicial
        self.x_positions = {"left": 300, "down": 420, "up": 540, "right": 660}
        self.x = self.x_positions[direction]
        self.y = -100

        # Spritesheet das notas (carregado uma vez na game.py)
        self.spritesheet = None
        self.current_frame = 0
        self.animation_speed = 12  # fps da animação da nota

    def set_spritesheet(self, spritesheet: SpriteSheet):
        self.spritesheet = spritesheet

    def update(self, dt: float, song_position: float):
        if self.hit or self.miss:
            self.alpha = max(0, self.alpha - 800 * dt)
            return

        # Movimento da nota
        distance = (self.time - song_position) * (self.speed / 1000.0)
        self.y = 500 - distance

        # Animação da nota (scrolando)
        self.current_frame = int((pygame.time.get_ticks() / 1000.0) * self.animation_speed) % 4

    def draw(self, surface: pygame.Surface):
        if not self.spritesheet:
            # Fallback colorido
            colors = {"left": (0, 255, 255), "down": (0, 255, 0),
                      "up": (255, 255, 0), "right": (255, 0, 255)}
            color = colors[self.direction]
            s = pygame.Surface((90, 90), pygame.SRCALPHA)
            pygame.draw.rect(s, color, (0, 0, 90, 90), border_radius=12)
            s.set_alpha(self.alpha)
            surface.blit(s, (self.x, self.y))
            return

        # Desenha frame da animação
        frame = self.spritesheet.get_frame(f"arrow{self.direction.capitalize()}", self.current_frame)
        frame.set_alpha(self.alpha)
        surface.blit(frame, (self.x, self.y))

    def should_remove(self, song_position: float) -> bool:
        return self.y > 800 or (self.time + 500 < song_position and not self.hit)