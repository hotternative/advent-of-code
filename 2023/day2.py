import re

def is_possible(blue: int, red: int, green: int):
    return all([blue <= 14 and green <= 13 and red <= 12])

def get_counts(round: str):

    counts = {"blue": 0, "red": 0, "green": 0}
    for colour in counts.keys():
        pattern = re.compile(rf'(\d+)(?= {colour})')
        match = pattern.search(round)
        if match:
            counts[colour] = int(match.group())
    return counts.values()

def part1():
    with open("2.input") as f:
        lines = f.readlines()
        ans = 0
        for line in lines:
            game, info = line.split(":")
            _, game_no = game.split(" ")
            rounds = info.split(";")
            min_colour_required = {"blue": 0, "red": 0, "green": 0}
            for round in rounds:
                blue, red, green = get_counts(round)
                if not is_possible(blue, red, green):
                    break
            else:
                ans += int(game_no)

def part2():
    with open("2.input") as f:
        lines = f.readlines()
        ans = 0
        for line in lines:
            game, info = line.split(":")
            _, game_no = game.split(" ")
            rounds = info.split(";")
            min_colour_required = {"blue": 0, "red": 0, "green": 0}
            power = 1
            for round in rounds:
                blue, red, green = get_counts(round)
                if min_colour_required['blue'] < blue:
                    min_colour_required['blue'] = blue
                if min_colour_required['red'] < red:
                    min_colour_required['red'] = red
                if min_colour_required['green'] < green:
                    min_colour_required['green'] = green
            for v in min_colour_required.values():
                power *= v

            ans += power

        print(ans)
