import re

def has_special_chars(input):
    pattern = re.compile(r"[^a-zA-Z0-9.\s]")
    return bool(pattern.search(input))


def find_numbers(input):
    pattern = re.compile(r"\d+")
    return re.finditer(pattern, input)


def is_part_number(start, end, lines, i):
    surroundings = ""
    # for c in range(start, end):
    #     for x in range(c-1, c+2):
    #         for y in range(j-1, j+2):
    left = start - 1 if start > 0 else 0  # the index of the char on the left boundary
    right = end + 1 if end < len(lines[i]) else end  # the index of the char on the right boundary

    if i > 0:
        surroundings += lines[i - 1][left:right]
    if i < len(lines) - 1:
        surroundings += lines[i + 1][left:right]
    if start > 0:
        surroundings += lines[i][start - 1]
    if end < len(lines[i]):
        surroundings += lines[i][end]

    return has_special_chars(surroundings)


def part1():
    ans = 0
    with open("3.input") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for match in find_numbers(line):
                if is_part_number(match.start(), match.end(), lines, i):
                    ans += int(match.group())
    print(ans)




def find_trailing_numbers(input):
    pattern = re.compile(r"\d+$")
    return re.search(pattern, input)


def find_leading_numbers(input):
    pattern = re.compile(r"^\d+")
    return re.search(pattern, input)

def find_parts(i, j, lines):
    parts = []
    if match := find_trailing_numbers(lines[i][:j]):
        parts.append(match.group())

    if match := find_leading_numbers(lines[i][j+1:]):
        parts.append(match.group())

    if i > 0:
        for match in find_numbers(lines[i-1]):
            if j - 1 <= match.start() <= j + 1 or j <= match.end() <= j + 2:
                parts.append(match.group())

    if i < len(lines) - 1:
        for match in find_numbers(lines[i + 1]):
            if j - 1 <= match.start() <= j + 1 or j <= match.end() <= j + 2:
                parts.append(match.group())

    return parts


def part2():
    ans = 0
    with open("3.input") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == "*":
                    adjacent_parts = find_parts(i, j, lines)
                    if len(adjacent_parts) == 2:
                        ans += int(adjacent_parts[0]) * int(adjacent_parts[1])
    print(ans)

if __name__ == "__main__":
    part2()
