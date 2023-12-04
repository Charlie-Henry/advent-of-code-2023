from string import ascii_letters
from ballgame import ballgame

# loading game data into objects
games = []
with open("input.txt") as infile:
    for line in infile:
        rounds = line.split(":")[1].replace(" ", "").split(";")
        g = ballgame(game_id=int(line.split(":")[0].split("Game ")[1]))
        # Processes each round
        for r in rounds:
            cubes = r.split(",")
            green = 0
            blue = 0
            red = 0
            # processing each color
            for b in cubes:
                # h/t https://stackoverflow.com/a/26553271
                # removes all ascii chars from the string to get the integer value
                ball_val = int(b.strip().rstrip(ascii_letters))
                if "green" in b:
                    green += ball_val
                elif "red" in b:
                    red += ball_val
                elif "blue" in b:
                    blue += ball_val
            g.add_round(red=red, blue=blue, green=green)
        games.append(g)


total = 0
for g in games:
    if g.is_valid():
        total += g.get_id()


print(f"Part 1 answer: {total}")

total = 0
for g in games:
    total += g.get_min_cubes_required()

print(f"Part 2 answer: {total}")


