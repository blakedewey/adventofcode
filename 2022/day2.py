def main(input_filename):
    # Define Rules
    rules = {'A': {'X': 4, 'Y': 8, 'Z': 3},
             'B': {'X': 1, 'Y': 5, 'Z': 9},
             'C': {'X': 7, 'Y': 2, 'Z': 6}}
    choice = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
              'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
              'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}}
    
    # Loop through games
    part1_score = 0
    part2_score = 0
    for line in open(input_filename):
        p1, p2 = line.strip().split(' ')
        part1_score += rules[p1][p2]
        part2_score += rules[p1][choice[p1][p2]]
    return part1_score, part2_score


if __name__ == '__main__':
    print(main('data/day2.txt'))