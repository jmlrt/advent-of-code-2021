with open("input.txt") as f:
    lines = f.readlines()

h_pos = 0
depth = 0

for i in range(0, len(lines)):
    move, scount = lines[i].split()
    count = int(scount)
    if move == "forward":
        h_pos += count
    if move == "down":
        depth += count
    if move == "up":
        depth -= count
    print(f"{h_pos=}, {depth=}")
print(f"Answer: {h_pos * depth}")
