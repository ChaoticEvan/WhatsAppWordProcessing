import sys
from utils import process_line

file_path = sys.argv[1]
file = open(file_path, encoding="utf8")

lines = file.readlines()
message1 = ""
for line in lines:
    message1 = process_line(line)

print(message1)

