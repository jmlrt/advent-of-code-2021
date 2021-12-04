with open("input.txt") as f:
    lines = f.readlines()

c = 0
inc = 0

while c < len(lines):
    if int(lines[c]) - int(lines[c - 1]) > 0:
        inc += 1
    c += 1
print(f"Answer: {inc}")
