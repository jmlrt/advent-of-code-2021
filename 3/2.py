# FILE = 'example.txt'
FILE = "input.txt"


def get_bit_code(list, bit):
    # print(f'{list=}, {bit=}')
    zeros = []
    ones = []
    for i in range(0, len(list)):
        code = list[i]
        if code[bit] == "0":
            zeros.append(code)
        if code[bit] == "1":
            ones.append(code)
    # print(f'{zeros=}, {ones=}')
    return zeros, ones


def filter_codes(list, type):
    pos = 0
    while len(list) > 1:
        zeros = []
        ones = []
        zeros, ones = get_bit_code(list, pos)

        if type == "oxygen":
            if len(zeros) > len(ones):
                list = zeros
            else:
                list = ones
        if type == "co2":
            if len(zeros) <= len(ones):
                list = zeros
            else:
                list = ones
        pos += 1
    return list[0]


with open(FILE) as f:
    numbers = f.readlines()

oxygen = filter_codes(numbers, "oxygen")
co2 = filter_codes(numbers, "co2")
print(f"{oxygen=}, {co2=}")

print(f"Answer: {int(oxygen, 2) * int(co2, 2)}")
