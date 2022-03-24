import sys
from utils import process_line, remove_word

file_path = sys.argv[1]
file = open(file_path, encoding="utf8")

lines = file.readlines()
processed_lines = list()
for line in lines:
    processed_lines.append(process_line(line))

csv = open(sys.argv[2], 'w', encoding="utf8")

for name, message in processed_lines:
    if "Evan" not in name:
        continue
    csv.write(message)

csv.close()