# engine/chart.py
import json
from engine.note import Note

class Chart:
    def __init__(self, json_path: str):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Formato Psych Engine
        self.song_name = data.get("song", "Unknown")
        self.bpm = data.get("bpm", 150.0)
        self.offset = data.get("offset", 0.0)
        self.notes_data = data.get("notes", [])

        print(f"📊 Chart carregado: {self.song_name} | BPM: {self.bpm} | Seções: {len(self.notes_data)}")

    def generate_notes(self):
        notes = []
        for section in self.notes_data:
            for note_data in section.get("sectionNotes", []):
                if len(note_data) < 2:
                    continue
                
                time = note_data[0]        # tempo em milissegundos
                note_type = int(note_data[1])  # 0 = left, 1 = down, etc.
                length = note_data[2] if len(note_data) > 2 else 0

                directions = ["left", "down", "up", "right"]
                direction = directions[note_type % 4]

                note = Note(time=time, direction=direction)
                notes.append(note)

        return sorted(notes, key=lambda n: n.time)