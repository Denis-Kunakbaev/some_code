from pathlib import Path
import json


def json_reader(self):
    current_dir = Path(__file__).parent.resolve()
    file_path = current_dir / 'Resources' / 'configs.json'
    with open(file_path, 'r') as f:
        self.data = json.load(f)
    return self.data