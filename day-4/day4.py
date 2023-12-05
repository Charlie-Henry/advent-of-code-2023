# part 1
total = 0
cards = {}
with open("input.txt") as infile:
    for line in infile:
        winning_text, our_text = line.split(":")[1].split("|")
        card_id = int(line.split(":")[0].replace(" ","").split("Card")[1])
        winning_numbers = []
        our_numbers = []
        for num in winning_text.strip().split(" "):
            if num:
                winning_numbers.append(int(num))

        value = 0
        for num in our_text.strip().split(" "):
            if num:
                our_numbers.append(int(num))
                if int(num) in winning_numbers:
                    if value == 0:
                        value = 1
                    else:
                        value = value * 2
        cards[card_id] = [winning_numbers, our_numbers]

        total += value

print(f"part 1 answer: {total}")

# part 2
# create initial card stack
card_stack = []
for key in cards:
    cards[key].append(key)
    card_stack.append(cards[key])


count = 0
while card_stack:
    curr_card = card_stack.pop(0)
    count += 1
    winning_numbers = curr_card[0]
    our_numbers = curr_card[1]
    card_id = curr_card[2]
    matching_numbers = 0
    for num in our_numbers:
        if num in winning_numbers:
            matching_numbers += 1

    if matching_numbers > 0:
        for i in range(card_id+1, card_id+matching_numbers+1):
            card_stack.insert(0, cards[i])

print(f"part 2 answer: {count}")





