import pygame
from engine.chart import Chart
from engine.note import Note
from engine.conductor import Conductor
from engine.input import KEY_MAP

class PlayState:
    def __init__(self, screen):
        self.screen = screen

        self.chart = Chart("assets/2015/2015-normal.json")
        self.conductor = Conductor(self.chart.bpm)

        self.notes = [Note(n["time"], n["dir"]) for n in self.chart.notes]

        self.music = pygame.mixer.Sound("assets/2015/music.mp3")

        self.paused = False

        self.start()

    def start(self):
        self.music.play()
        self.conductor.start()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused

                if not self.paused:
                    self.check_hit(event.key)

    def update(self):
        if self.paused:
            return

        time = self.conductor.get_time()

        for note in self.notes:
            note.update(time)

    def draw(self):
        self.screen.fill((0, 0, 0))

        for note in self.notes:
            note.draw(self.screen)

    def check_hit(self, key):
        if key not in KEY_MAP:
            return

        direction = KEY_MAP[key]

        for note in self.notes:
            if note.direction == direction:
                if abs(self.conductor.get_time() - note.time) < 150:
                    note.hit = True
                    break