from pathlib import Path
import json

path = Path('numbers.json')
try:
    contents = path.read_text()
    print(contents)
    print(contents[0])
    info = json.loads(contents)
    print(info[0])
except FileNotFoundError:
    print(f"{path} not found")