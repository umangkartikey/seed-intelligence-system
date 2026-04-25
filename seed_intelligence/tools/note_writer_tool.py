from pathlib import Path
import time


class NoteWriterTool:
    name = "note_writer"
    risk = "medium"

    def __init__(self, path="seed_notes.txt"):
        self.path = Path(path)

    def run(self, input_data):
        note = input_data.get("note", "")

        if not note:
            return {"ok": False, "error": "Empty note"}

        with self.path.open("a", encoding="utf-8") as f:
            f.write(f"\n[{time.ctime()}] {note}")

        return {"ok": True, "saved_to": str(self.path)}
