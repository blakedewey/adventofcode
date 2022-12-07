def main(input_filename):
    datastream = open(input_filename).read()
    marker = []
    marker_len = 4
    positions = []
    for i, char in enumerate(datastream):
        if char not in marker:
            marker.append(char)
            if len(marker) == marker_len:
                positions.append(i+1)
                if marker_len == 4:
                    marker_len = 14
                else:
                   return positions
        else:
            marker = [char]
        

if __name__ == '__main__':
    print(main('data/day6.txt'))
