from soil_params import get_parameters

params = get_parameters("input")

mapping_flow = [
    {
        "start": "seeds",
        "mapping": "seed_to_soil",
        "end": "soil",
    },
    {
        "start": "soil",
        "mapping": "soil_to_fertilizer",
        "end": "fertilizer",
    },
    {
        "start": "fertilizer",
        "mapping": "fertilizer_to_water",
        "end": "water",
    },
    {
        "start": "water",
        "mapping": "water_to_light",
        "end": "light",
    },
    {
        "start": "light",
        "mapping": "light_to_temperature",
        "end": "temperature",
    },
    {
        "start": "temperature",
        "mapping": "temperature_to_humidity",
        "end": "humidity",
    },
    {
        "start": "humidity",
        "mapping": "humidity_to_location",
        "end": "location",
    },
]

for step in mapping_flow:
    ranges = params[step["mapping"]]

    data = []
    for row in ranges:
        dest_range_start = row[0]
        source_range_start = row[1]
        range_len = row[2]

        source = range(source_range_start, source_range_start + range_len)
        dest = range(dest_range_start, dest_range_start + range_len)
        data.append([source, dest])


    step["map"] = data

data = {"seeds": params["seeds"]}

for map in mapping_flow:
    start_ids = data[map["start"]]
    ending_ids = []
    for source_id in start_ids:
        output_id = None
        for row in map["map"]:
            if source_id in row[0]:
                i = row[0].index(source_id)
                output_id = row[1][i]
        if not output_id:
            output_id = source_id
        ending_ids.append(output_id)

    data[map["end"]] = ending_ids

print(f"Part 1: {min(data['location'])}")

# part 2

data = {}
seeds = []
for i in range(len(params["seeds"])):
    if i % 2 == 0:
        start = params["seeds"][i]
    else:
        seeds.append(range(start, start + params["seeds"][i]))

print(len(seeds))

min_locs = []
mapping_flow.reverse()
for map in mapping_flow:
    for i in map["map"]:
        for start_loc in i[1]:
            start_loc




print(f"part 2 answer: {min(min_locs)}")

