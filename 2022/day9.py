def main(input_filename, n):
    with open(input_filename) as fp:
        instructs = [line.strip().split() for line in fp]
    pos = [[0, 0] for _ in range(n)]
    tlocs = set([(0, 0)])
    for dir, dist in instructs:
        for _ in range(int(dist)):
            match dir:
                case 'R':
                    pos[0][0] += 1
                case 'L':
                    pos[0][0] -= 1
                case 'U':
                    pos[0][1] += 1
                case 'D':
                    pos[0][1] -= 1
            for i in range(1, n):
                dx, dy = pos[i-1][0]-pos[i][0], pos[i-1][1]-pos[i][1]
                if -1 <= dx <= 1 and -1 <= dy <= 1:
                    continue
                if dx != 0:
                    pos[i][0] += -1 if dx < 0 else 1
                if dy != 0:
                    pos[i][1] += -1 if dy < 0 else 1
            tlocs.add(tuple(pos[n-1]))
    return len(tlocs)


if __name__ == '__main__':
    print(main('data/day9.txt', 2), main('data/day9.txt', 10))