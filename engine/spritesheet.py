# engine/spritesheet.py
import pygame
import xml.etree.ElementTree as ET

class SpriteSheet:
    def __init__(self, image_path: str, xml_path: str = None):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.frames = {}

        if xml_path:
            self._load_xml(xml_path)

    def _load_xml(self, xml_path: str):
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for sub in root.findall("SubTexture"):
            name = sub.get("name")
            x = int(sub.get("x"))
            y = int(sub.get("y"))
            w = int(sub.get("width"))
            h = int(sub.get("height"))

            # Suporte a sprites recortados (trimmed)
            frame_x = int(sub.get("frameX", 0))
            frame_y = int(sub.get("frameY", 0))
            frame_w = int(sub.get("frameWidth", w))
            frame_h = int(sub.get("frameHeight", h))

            frame = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA)
            frame.blit(self.image, (frame_x, frame_y), (x, y, w, h))

            # Nome base (arrowLeft, arrow-down-receptor, etc)
            base_name = ''.join(c for c in name if not c.isdigit()).rstrip('_')
            
            if base_name not in self.frames:
                self.frames[base_name] = []
            self.frames[base_name].append(frame)

    def get_frame(self, name: str, index: int = 0):
        frames = self.frames.get(name, [])
        return frames[index % len(frames)] if frames else None