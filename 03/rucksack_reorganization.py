f = open("03/input.txt")

rucksacks = []
all_char_counts = []

f.seek(0)

for rucksack in f:
    mid = len(rucksack) // 2
    compartment1 = rucksack[:mid]
    compartment2 = rucksack[mid:]
    rucksacks.append([[compartment1], [compartment2]])

f.close()

for rucksack in rucksacks:
    char_counts = {}
    for char in rucksack[0][0]:
        if char in rucksack[1][0]:
            if char not in char_counts:
                count1 = rucksack[0][0].count(char)
                count2 = rucksack[1][0].count(char)
                char_counts[char] = min(count1, count2)

    all_char_counts.append(char_counts)

def char_value(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27

total_sum = 0

for char_counts in all_char_counts:
    for char, _ in char_counts.items():
        total_sum += char_value(char)

print(total_sum)