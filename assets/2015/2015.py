import pygame
from engine.chart import Chart
from engine.spritesheet import SpriteSheet

def play(game):
    print("🎵 Iniciando Fase: 2015")

    try:
        game.chart = Chart("assets/2015/2015-easy.json")

        game.conductor.load_song(
            inst_path="assets/2015/inst.ogg",
            bpm=game.chart.bpm,
            offset=getattr(game.chart, 'offset', 0.0)
        )

        game.notes = game.chart.generate_notes()

        print(f"🧠 Total de notas: {len(game.notes)}")
        if len(game.notes) > 0:
            print(f"Primeira nota em: {game.notes[0].time} ms")

        game.note_spritesheet = SpriteSheet(
            "assets/images/notes/arrows.png",
            "assets/images/notes/arrows.xml"
        )

        game.receptor_spritesheet = SpriteSheet(
            "assets/images/notes/arrows-receptors.png",
            "assets/images/notes/arrows-receptors.xml"
        )

        for note in game.notes:
            note.set_spritesheet(game.note_spritesheet)

        # NÃO VOU MEXER NOS RECEPTORES 😇
        game.receptors = {
            "left":  pygame.Rect(690, 73, 110, 110),
            "down":  pygame.Rect(820, 73, 110, 110),
            "up":    pygame.Rect(940, 73, 110, 110),
            "right": pygame.Rect(1065, 73, 110, 110),
        }

        game.change_state("playing")

        # IMPORTANTE: usar music ao invés de Sound
        pygame.mixer.music.load("assets/2015/inst.ogg")
        pygame.mixer.music.play()

        game.conductor.start_time = pygame.time.get_ticks()

        print("✅ Fase 2015 carregada (timing sincronizado)")

    except Exception as e:
        print(f"❌ Erro na fase 2015: {e}")
        import traceback
        traceback.print_exc()