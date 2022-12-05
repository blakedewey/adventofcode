def main(input_filename):
    complete_count = 0
    overlap_count = 0
    for line in open(input_filename):
        x1, x2, y1, y2 = map(int, line.replace(',', '-').split('-'))
        overlap_count += not (x2 < y1 or x1 > y2)
        complete_count += (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2)
    return complete_count, overlap_count


def alt(input_filename):
    complete_count = 0
    overlap_count = 0
    for line in open(input_filename):
        range1, range2 = [range(*[int(limit) + i for i,limit in enumerate(range_str.split('-'))]) for range_str in line.strip().split(',')]
        overlap = set(range1).intersection(range2)
        overlap_count += len(overlap) > 0
        complete_count += len(overlap) == len(range1) or len(overlap) == len(range2)
    return complete_count, overlap_count


if __name__ == '__main__':
    print(main('data/day4.txt'))