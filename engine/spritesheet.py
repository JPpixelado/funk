# engine/spritesheet.py
import pygame
import xml.etree.ElementTree as ET
from typing import Dict, List, Tuple

class SpriteSheet:
    def __init__(self, image_path: str, xml_path: str = None):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.frames: Dict[str, List[pygame.Surface]] = {}
        self.frame_data: Dict[str, List[Dict]] = {}
        
        if xml_path:
            self._load_xml(xml_path)

    def _load_xml(self, xml_path: str):
        """Carrega atlas Sparrow v2 (formato oficial do FNF)"""
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        for sub in root.findall("SubTexture"):
            name = sub.get("name")
            x = int(sub.get("x"))
            y = int(sub.get("y"))
            w = int(sub.get("width"))
            h = int(sub.get("height"))
            
            # Recorta o frame
            frame = pygame.Surface((w, h), pygame.SRCALPHA)
            frame.blit(self.image, (0, 0), (x, y, w, h))
            
            # Remove o sufixo numérico para agrupar animações (ex: "arrowLeft0001" → "arrowLeft")
            base_name = ''.join([c for c in name if not c.isdigit()]).rstrip('_')
            
            if base_name not in self.frames:
                self.frames[base_name] = []
                self.frame_data[base_name] = []
            
            self.frames[base_name].append(frame)
            self.frame_data[base_name].append({
                "name": name,
                "x": x, "y": y, "w": w, "h": h
            })

    def get_animation(self, name: str) -> List[pygame.Surface]:
        """Retorna lista de frames de uma animação"""
        return self.frames.get(name, [])

    def get_frame(self, animation: str, index: int) -> pygame.Surface:
        """Retorna um frame específico"""
        frames = self.get_animation(animation)
        if frames:
            return frames[index % len(frames)]
        return pygame.Surface((50, 50), pygame.SRCALPHA)  # fallback