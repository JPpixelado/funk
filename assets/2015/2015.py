# assets/2015/2015.py
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

        # RECEPTORES 64x64 com espaçamento bom
        game.receptors = {
            "left":  pygame.Rect(320, 498, 64, 64),
            "down":  pygame.Rect(390, 498, 64, 64),
            "up":    pygame.Rect(500, 498, 64, 64),
            "right": pygame.Rect(608, 498, 64, 64),
        }

        game.change_state("playing")
        game.conductor.play()

        print("✅ Fase 2015 carregada (64×64)")

    except Exception as e:
        print(f"❌ Erro na fase 2015: {e}")
        import traceback
        traceback.print_exc()