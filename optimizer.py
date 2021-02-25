import re
from collections import Counter

def find_solution(time, intsec_dict, intsec_count, path, sensitivity):
    street_volumes = calculate_volumes(path)
    blocksize = time/sensitivity
    intsec_weightings = []
    for intsec_num in range(intsec_count):
        intersection = intsec_dict[str(intsec_num)]
        this_intsec_weights = []
        for road in intersection[1]:
            try:
                volume = street_volumes[road]
            except Exception as identifier:
                volume = 0
            normalised_volumes = int((volume - 1) // blocksize + 1) 
            if normalised_volumes > 0:
                this_intsec_weights.append((road, normalised_volumes))
        if len(this_intsec_weights) == 0:
            this_intsec_weights.append((intersection[1][0], 1))
        intsec_weightings.append(this_intsec_weights)
    return intsec_weightings


def calculate_volumes(path) -> dict:
    with open(path) as f:
        no_roads = f.readline().split(' ')[2]
        for i in range(int(no_roads)):
            next(f)
        data = f.read()
    streets = re.findall(r'[a-z-]+', data)
    street_count = Counter(streets)
    return dict(street_count)

# calculate_volumes('./datasets/a.txt')