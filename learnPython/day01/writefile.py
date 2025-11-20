from pathlib import Path

path = Path('hello.txt')
contents = '''
hello world!
hello world!  a
hello world!
'''
path.write_text(contents)