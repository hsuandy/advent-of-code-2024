with open("inputs/day_1_input.txt", "r") as input_file:
    left = []
    right = []
    score = []
    distances = [line.split() for line in input_file]
    
    for distance in distances:
        l, r = distance
        left.append(int(l))
        right.append(int(r))

    for num_l in left:
        sim_score = 0
        for num_r in right:
            if num_r == num_l:
                sim_score += 1
        score.append(num_l * sim_score)
                     
    print(sum(score))
    