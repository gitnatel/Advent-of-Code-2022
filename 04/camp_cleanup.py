f = open("04/input.txt")

assignment_list = []

f.seek(0)

for assignment in f:
    stripped_assignment = assignment.strip().split(',')
    pair_list = []
    for assignment in stripped_assignment:
        assignment = [int(num) for num in assignment.split('-')]
        pair_list.append(assignment)
        if len(pair_list) == 2:
            assignment_list.append(pair_list)
            pair_list = []

f.close()

count = 0
for pair in assignment_list:
    if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]):
        count += 1

print("the number of assignments that fully overlap another within a pair: " + str(count))