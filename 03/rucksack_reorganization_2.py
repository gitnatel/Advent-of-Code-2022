f = open("03/input.txt")

rucksacks = []
common_chars_list = []

f.seek(0)

for rucksack in f:
    rucksacks.append([rucksack.strip()])

f.close()

for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    group_chars = []
    for rucksack in group:
        group_chars.append(list(rucksack[0]))
    common_chars = list(set(group_chars[0]).intersection(*group_chars))

    common_chars_list.append([common_chars])

def group_value(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27

total_sum = 0

for char_list in common_chars_list:
    for char in char_list[0]:
        total_sum += group_value(char)

print(total_sum)