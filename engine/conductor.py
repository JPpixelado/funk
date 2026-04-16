# engine/conductor.py
import pygame

class Conductor:
    def __init__(self):
        self.song_position = 0.0
        self.bpm = 100.0
        self.crochet = 0.0  # tempo de um beat
        self.song_started = False
        self.paused = False
        self.music = None

    def load_song(self, inst_path: str, bpm: float, offset: float = 0.0):
        self.bpm = bpm
        self.crochet = 60.0 / bpm
        self.offset = offset
        self.music = pygame.mixer.Sound(inst_path)

    def play(self):
        if self.music:
            self.music.play()
            self.song_started = True

    def update(self, dt: float):
        if self.song_started and not self.paused:
            self.song_position += dt * 1000  # em milissegundos