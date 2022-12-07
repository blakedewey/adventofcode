def main(input_filename):
    pwd = []
    dirsizes = {}
    for line in open(input_filename).read().split('$ ')[1:]:
        line = line.strip()
        if line.startswith('cd'):
            if line.endswith('..'):
                del pwd[-1]
            else:
                pwd.append(line[3:].rstrip('/'))
                dirsizes[tuple(pwd)] = 0
        else:
            dirsize = sum([int(item.split(' ')[0]) 
                           for item in line.split('\n')[1:]
                           if not item.startswith('dir')])
            dirsizes[tuple(pwd)] += dirsize
            for i in range(1, len(pwd)):
                dirsizes[tuple(pwd[:-i])] += dirsize
    p1_ans = sum([dirsize for dirsize in dirsizes.values() if dirsize <= 100000])
    needed_space = 30000000 - (70000000 - dirsizes[('',)])
    p2_ans = min([dirsize for dirsize in dirsizes.values() if dirsize >= needed_space])
    return p1_ans, p2_ans


if __name__ == '__main__':
    print(main('data/day7.txt'))
