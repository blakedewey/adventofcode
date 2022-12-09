def main(input_filename):
    trees = list(map(list, open(input_filename).read().split('\n')[:-1]))
    
    visible = []
    scenic = []
    for i, row in enumerate(trees):
        row = list(map(int, row))
        visible.append([False]*len(row))
        scenic.append([1] * len(trees[0]))
        max_height = -1
        last_tree = [0] * 10
        for j, tree in enumerate(row):
            if tree > max_height:
                visible[i][j] = True
                max_height = tree
            scenic[i][j] = j - last_tree[tree]
            last_tree[:tree+1] = [j] * (tree + 1)
        max_height = -1
        last_tree = [len(row)-1] * 10
        for j, tree in sorted(enumerate(row), reverse=True):
            if tree > max_height:
                visible[i][j] = True
                max_height = tree
            scenic[i][j] *= last_tree[tree] - j
            last_tree[:tree+1] = [j] * (tree + 1)
    
    trees = list(zip(*trees))
    for i, col in enumerate(trees):
        col = list(map(int, col))
        max_height = -1
        last_tree = [0] * 10
        for j, tree in enumerate(col):
            if tree > max_height:
                visible[j][i] = True
                max_height = tree
            scenic[j][i] *= j - last_tree[tree]
            last_tree[:tree+1] = [j] * (tree + 1)
        max_height = -1
        last_tree = [len(row)-1] * 10
        for j, tree in sorted(enumerate(col), reverse=True):
            if tree > max_height:
                visible[j][i] = True
                max_height = tree
            scenic[j][i] *= last_tree[tree] - j
            last_tree[:tree+1] = [j] * (tree + 1)
    
    return (sum([sum(row) for row in visible]),
            max([max(row) for row in scenic]))


if __name__ == '__main__':
    print(main('data/day8.txt'))