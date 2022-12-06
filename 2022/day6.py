def main(input_filename):
    datastream = open(input_filename).read()
    marker = []
    marker_len = 4
    positions = []
    for i,char in enumerate(datastream):
        if char in marker:
            marker = []
        marker.append(char)
        if len(marker) == marker_len:
            positions.append(i+1)
            if marker_len == 4:
                marker_len = 14
            else:
                return positions

if __name__ == '__main__':
    main('data/day6.txt')