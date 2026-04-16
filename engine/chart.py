# engine/chart.py
import json
from engine.note import Note

class Chart:
    def __init__(self, json_path: str):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.song_name = data.get("song", {}).get("song", "Unknown")
        self.bpm = data.get("song", {}).get("bpm", 100.0)
        self.offset = data.get("song", {}).get("offset", 0.0)
        self.notes_data = data.get("song", {}).get("notes", [])
        
    def generate_notes(self):
        notes = []
        for section in self.notes_data:
            for note_data in section.get("sectionNotes", []):
                time = note_data[0]      # tempo em ms
                data = note_data[1]      # índice da nota (0=left, 1=down, etc.)
                length = note_data[2]    # sustain length
                
                directions = ["left", "down", "up", "right"]
                direction = directions[data % 4]
                
                note = Note(time=time, direction=direction)
                notes.append(note)
        return sorted(notes, key=lambda n: n.time)