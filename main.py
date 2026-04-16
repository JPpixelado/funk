# main.py
import pygame
import sys
from engine.game import Game

def main():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 512)
    
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("FNFK - Sexta à Noite do Funk")
    clock = pygame.time.Clock()
    
    game = Game(screen, clock)
    
    try:
        game.run()
    except Exception as e:
        print(f"Erro fatal: {e}")
    finally:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()