import re
from typing import List

# A naive way to solve this problem is to use a loop to iterate through each line in order and find the first digit,
# and then iterate throught in reverse order to find the last digit.
def part_1():
    with open("1.input") as f:
        lines = f.readlines()
        ans = 0
        for line_no, line in enumerate(lines):
            for i in range(len(line)):
                if line[i].isdigit():
                    match = re.search(r"^\D*(\d)", line)
                    if match.group(1) != line[i]:
                        print(f"first digit not match. From regex: {match.group(1)}, from line: {line[i]}")
                        print(line)
                    ans += int(line[i]) * 10
                    break
            else:
                raise ValueError("No digit found")
            for j in range(len(line) - 1, -1, -1):
                if line[j].isdigit():
                    match = re.search(r"(\d)\D*$", line)
                    if match.group(1) != line[j]:
                        print(f"last digit not match. From regex: {match.group(1)}, from line: {line[j]}")
                        print(line)
                    ans += int(line[j])
                    break
            else:
                raise ValueError("No digit found")
        print(ans)

number_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def re_match(string):
    vals = [str(i) for i in list(number_dict.values())]
    chars_to_searches = list(number_dict.keys()) + vals
    chars_to_search = "|".join(chars_to_searches)
    pattern = re.compile(rf'(?=({chars_to_search}))')
    match = re.findall(pattern, string)
    return match


def part_2():

    # def first_index(string, chars_to_searches: List[str]):
    #     finds = [string.find(chars) for chars in chars_to_searches if string.find(chars) != -1]
    #     return min(finds)
    #
    # def last_index(string, chars_to_searches: List[str]):
    #     finds = [string.rfind(chars) for chars in chars_to_searches if string.rfind(chars) != -1]
    #     return max(finds)
    #
    # def first_match(string, chars_to_searches: List[str]):
    #     pattern = re.compile(r"(" + "|".join(chars_to_searches) + ")")
    #     match = pattern.search(string)
    #     return match
    #
    # def last_match(string, chars_to_searches: List[str]):
    #     pattern = re.compile(r"(" + "|".join(chars_to_searches) + "\D*$" + ")")
    #     match = pattern.search(string)
    #     return match


    with open("1.input") as f:
        lines = f.readlines()
        ans = 0


        for i, line in enumerate(lines, 1):
            matches = re_match(line)
            if not matches:
                raise ValueError("No match found")
            # print(matches)

            if matches[0] in number_dict:
                tens = number_dict[matches[0]] * 10
                ans += tens
            else:
                tens = int(matches[0]) * 10
                ans += tens

            if matches[-1] in number_dict:
                ones = number_dict[matches[-1]]
                ans += ones
            else:
                ones = int(matches[-1])
                ans += ones

            print(i, tens+ones)

        print(ans)

if __name__ == "__main__":
    # part_1()
    part_2()
    # 28380 is too low
    # 53355 is too high

#
# import unittest
# class TestSolution(unittest.TestCase):
#     def test996(self):
#         string = "jjpngnpzglkbltbrv2tjmqrpb"
#         matches = re_match(string)
#         assert matches[0] == "2"
#         assert matches[-1] == "2"
#


