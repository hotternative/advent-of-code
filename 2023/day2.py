def is_possible(blue: int, red: int, green: int):
    return all([blue <= 14 and green <= 13 and red <= 12])


with open("2.input") as f:
    lines = f.readlines()

