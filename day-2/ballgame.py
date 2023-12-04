class ballgame():
    def __init__(self, game_id):
        self.game_id = game_id
        self.rounds = []
        self.red_cubes = 12
        self.blue_cubes = 14
        self.green_cubes = 13
        self.valid = True

    def add_round(self, red, green, blue):
        round_data = {
            "red": red,
            "blue": blue,
            "green": green,
        }
        if red > self.red_cubes or blue > self.blue_cubes or green > self.green_cubes:
            self.valid = False

        self.rounds.append(round_data)

    def is_valid(self):
        return self.valid

    def get_id(self):
        return self.game_id

    def get_min_cubes_required(self):
        min_r = []
        min_b = []
        min_g = []
        for r in self.rounds:
            min_r.append(r["red"])
            min_b.append(r["blue"])
            min_g.append(r["green"])
        return max(min_r) * max(min_b) * max(min_g)
