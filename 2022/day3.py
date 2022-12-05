def main(input_filename):
    # Load Data
    sacks = [line.strip() for line in open(input_filename)]
    scores = {chr(96+i):i for i in range(1, 27)} | {chr(64+i):i+26 for i in range(1, 27)}
    
    # Part 1
    total_priority = 0
    for sack in sacks:
        mid = len(sack) // 2
        (item,) = set(sack[:mid]).intersection(sack[mid:])
        total_priority += scores[item]
    
    # Part 2
    badge_priority = 0
    for group in range(0, len(sacks), 3):
        (badge,) = set(sacks[group]).intersection(sacks[group+1]).intersection(sacks[group+2])
        badge_priority += scores[badge]
    return total_priority, badge_priority


def alt(input_filename):
    # Load Data
    sacks = [line.strip() for line in open(input_filename)]
    
    # Part 1
    total_priority = 0
    for sack in sacks:
        mid = len(sack) // 2
        (item,) = set(sack[:mid]).intersection(sack[mid:])
        total_priority += ord(item) - (38 if ord(item) > 90 else 64)
    
    # Part 2
    badge_priority = 0
    for group in range(0, len(sacks), 3):
        (badge,) = set(sacks[group]).intersection(sacks[group+1]).intersection(sacks[group+2])
        badge_priority += ord(badge) - (38 if ord(badge) > 90 else 64)
    return total_priority, badge_priority


if __name__ == '__main__':
    print(main('data/day3.txt'))