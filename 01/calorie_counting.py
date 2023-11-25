f = open("01/input.txt")

elves = []
snacks = []

f.seek(0)

for snack in f:
    stripped_snack = snack.strip()
    if stripped_snack:
        snacks.append(stripped_snack)
    else:
        if snacks:
            elves.append(snacks)
            snacks = [] 

f.close()

if snacks:
    elves.append(snacks)

def calorie_count(elf):
    elf_calories = 0
    for snack in elf:
        elf_calories += int(snack)
    return elf_calories

calories_per_elf = []

for i, elf in enumerate(elves):
    elf_calories = calorie_count(elf)
    calories_per_elf.append([elf_calories])

def elf_with_highest_calories(elf_calories_list):
    max_calories = 0
    for elf_calories in elf_calories_list:
        if elf_calories[0] > max_calories:
            max_calories = elf_calories[0]
    return max_calories

calories = elf_with_highest_calories(calories_per_elf)
print(f'The elf with the highest calories is the elf with: {calories} calories')