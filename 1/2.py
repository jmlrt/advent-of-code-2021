def measure(i):
    return int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])


with open("input.txt") as f:
    lines = f.readlines()

c = 0
inc = 0

while c + 3 < len(lines):
    if measure(c + 1) - measure(c) > 0:
        inc += 1
    c += 1

print(f"Answer: {inc}")
