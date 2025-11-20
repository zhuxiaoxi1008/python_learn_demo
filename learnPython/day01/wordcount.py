from pathlib import Path

path = Path('Alice.txt')
contents = path.read_text(encoding='utf-8')
words = contents.split()
print(f"{len(words)}")