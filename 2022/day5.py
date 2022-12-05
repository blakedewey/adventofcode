def parse_input(input_filename):
    diagram, instructs = open(input_filename).read().split('\n\n')
    stacks = zip(*[row.split(' ') for row in diagram.replace('    ',' ').split('\n')[:-1]])
    stacks = [[item[1] for item in stack[::-1] if len(item) > 0] for stack in stacks]
    instructs = [line.split(' ') for line in instructs.split('\n')][:-1]
    instructs = [(int(arr[1]), int(arr[3])-1, int(arr[5])-1) for arr in instructs]
    return stacks, instructs

def main_p1(input_filename):
    stacks, instructs = parse_input(input_filename)
    for num, ind, new_ind in instructs:
        moved = reversed(stacks[ind][-num:])
        del stacks[ind][-num:]
        stacks[new_ind].extend(moved)
    return ''.join([stack[-1] for stack in stacks])

def main_p2(input_filename):
    stacks, instructs = parse_input(input_filename)
    for num, ind, new_ind in instructs:
        moved = stacks[ind][-num:]
        del stacks[ind][-num:]
        stacks[new_ind].extend(moved)
    return ''.join([stack[-1] for stack in stacks])


if __name__ == '__main__':
    print(main_p1('data/day4.txt'), main_p2('data/day4.txt'))