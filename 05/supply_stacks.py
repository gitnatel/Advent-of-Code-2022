f = open("05/input.txt")

stacks = [["Q","M","G","C","L"],["R","D","L","C","T","F","H","G"],["V","J","F","N","M","T","W","R"],["J","F","D","V","Q","P"],["N","F","M","S","L","B","T"],["R","N","V","H","C","D","P"],["H","C","T"],["G","S","J","V","Z","N","H","P"],["Z","F","H","G"]]
instruction_pos = 0
held_object = 0

initial_state = [stacks, instruction_pos, held_object]

instructions = []

f.seek(0)

for instruction in f:
    stripped_instruction = instruction.strip()
    instructions.append([stripped_instruction])

f.close()

filtered_instructions = []

for instruction in instructions:
    numbers = []
    for word in instruction[0].split():
        if word.isdigit():
            numbers.append(int(word))
    filtered_instructions.append(numbers)

# for instruction in filtered_instructions:


#
print(stacks)