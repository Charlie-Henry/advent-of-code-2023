import re
# Reading in data
data = []
with open("input.txt") as infile:
    for line in infile:
        data.append(line.strip())

def calculate_total_first_last(trebuchet_data):
    total = 0
    for entry in trebuchet_data:
        first = ""
        last = ""
        for char in entry:
            if char.isdigit():
                if not first:
                    first = char
                last = char

        total += int(f"{first}{last}")

    return total


print(f"part 1: {calculate_total_first_last(data)}")

# part 2
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

lookup_nums = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

for i in range(len(data)):
    row_indices = {}
    for val in numbers:
        # finding all occurrences of numbers in our text
        for m in re.finditer(val, data[i]):
            row_indices[m.start()] = val

    # replace the first letter of the number word with the digit
    output = list(data[i])
    for v in row_indices:
        output[v] = numbers[row_indices[v]]
    data[i] = str(output)

# part 2
print(f"part 2: {calculate_total_first_last(data)}")
