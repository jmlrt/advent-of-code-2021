with open("input.txt") as f:
    lines = f.readlines()

h_pos = 0
depth = 0
aim = 0

for i in range(0, len(lines)):
    move, scount = lines[i].split()
    count = int(scount)
    if move == "forward":
        h_pos += count
        depth += aim * count
    if move == "down":
        aim += count
    if move == "up":
        aim -= count
    print(f"{h_pos=}, {depth=}, {aim=}")
print(f"Answer: {h_pos * depth}")
