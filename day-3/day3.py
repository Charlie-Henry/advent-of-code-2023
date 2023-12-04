# Reading in data
data = []
with open("input.txt") as infile:
    for line in infile:
        data.append(line.strip())

row_width = len(data[0])
col_len = len(data)

# getting locations of all numbers and special characters
num_buffer = ""
row_id = 0
number_locations = []
special_char_locations = []

for row in data:
    col_id = 0
    for c in row:
        if c.isdigit():
            num_buffer = f"{num_buffer}{c}"
        elif c != ".":
            special_char_locations.append(
                {
                    "row": row_id,
                    "col": col_id,
                    "val": c
                }
            )
        if not c.isdigit():
            if num_buffer:
                number_locations.append(
                    {
                        "row": row_id,
                        "col": col_id,
                        "val": int(num_buffer)
                    }
                )
            num_buffer = ""
        col_id += 1
    if num_buffer:
        number_locations.append(
            {
                "row": row_id,
                "col": col_id,
                "val": int(num_buffer)
            }
        )
        num_buffer = ""
    row_id += 1

# grid search for special characters
total = 0
locations_searched = []
gear_locs = {}
for num in number_locations:
    col_ids = range(num["col"] - len(str(num["val"])) - 1,  num["col"] + 1)
    row_ids = range(num["row"] - 1,  num["row"] + 2)

    valid = False
    for c in col_ids:
        for r in row_ids:
            locations_searched.append([r, c])
            for s in special_char_locations:
                if s["row"] == r and s["col"] == c:
                    valid = True
                    # logging data for part 2
                    if s["val"] == "*":
                        if f"{s['row']}{s['col']}" in gear_locs:
                            gear_locs[f"{s['row']}{s['col']}"].append(num["val"])
                        else:
                            gear_locs[f"{s['row']}{s['col']}"] = [num["val"]]
    if valid:
        total += num["val"]

# visualization of search pattern
# vis = ""
# for r in range(col_len):
#     for c in range(row_width):
#         if [r,c] in locations_searched:
#             vis += "x"
#         else:
#             vis += "."
#     vis += "\n"
# print(vis)
print(f"part 1 answer {total}")

total = 0
for key in gear_locs:
    if len(gear_locs[key]) == 2:
        total += int(gear_locs[key][0]) * int(gear_locs[key][1])

print(f"part 2 answer {total}")

