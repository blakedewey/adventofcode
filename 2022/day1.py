def main(input_filename):
    calories = [[]]
    index = 0
    for line in open(input_filename):
        if line == '\n':
            calories[index] = sum(calories[index])
            calories.append([])
            index += 1
            continue
        calories[index].append(int(line.strip()))
    calories[index] = sum(calories[index])
    calories.sort()
    return calories[-1], sum(calories[-3:])


if __name__ == '__main__':
    print(main('data/day1.txt'))