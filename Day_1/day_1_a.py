with open("inputs/day_1_input.txt", "r") as input_file:
    left = []
    right = []
    distances = [line.split() for line in input_file]
    
    for distance in distances:
        l, r = distance
        left.append(int(l))
        right.append(int(r))

    print(sum([abs(pair[0] - pair[1]) for pair in zip(sorted(left), sorted(right))]))
    