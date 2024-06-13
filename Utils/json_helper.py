from pathlib import Path
import json

class JsonHelper:
    @staticmethod
    def read_json(path):
        # current_dir = Path(__file__).resolve().parent
        # root = current_dir.parent
        # file_path = root / 'Configs' / 'browser_settings.json'

        with open(path, 'r') as f:
            data = json.load(f)

        return data
    
    @staticmethod
    def write_json(path, data):
        with open(path, 'w') as file:
            json.dump(data, file, indent=3)
