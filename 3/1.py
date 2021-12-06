import numpy as np
from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()

# convert data to matrix list
matrix = []
for i in range(0, len(lines)):
    matrix.append(list(lines[i])[:-1])

# rotate matrix list
np_rot_matrix = np.rot90(np.array(matrix), -1)

# get most common for each bit
gamma_rate_bin = ""
epsilon_rate_bin = ""
for l in np_rot_matrix:
    most_common = Counter(l).most_common()[0]
    print(f"{most_common=}")
    least_common = Counter(l).most_common()[-1]
    print(f"{least_common=}")
    gamma_rate_bin += most_common[0]
    epsilon_rate_bin += least_common[0]

# convert from binary to decimal
gamma_rate = int(gamma_rate_bin, 2)
epsilon_rate = int(epsilon_rate_bin, 2)
print(f"{gamma_rate=}, {epsilon_rate=}")

print(f"Answer: {gamma_rate * epsilon_rate}")
