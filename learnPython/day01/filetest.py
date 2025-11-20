from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text().strip()

lines = contents.splitlines()
pi = ''
for line in lines: 
    pi += line.strip()
# print(len(pi))
# print(f"{pi[:52]}...")
birthday = input("Enter your birthday, in the form mmddyyyy: ")
if birthday in pi:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("not in pi ...")
     