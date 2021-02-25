import re
from collections import Counter

def find_solution(inputs):
    road_locations = {}
    for intersection in range(0, INTERSECTION_COUNT):
        for road in intersection[0]:
            road_locations[road] = intersection
    for car in cars:
        for road in cars:
            dictionary
    # for car in list of cars
    #   for road in car's route
    # add volume information to road

    # for intersection in intersections
    #   for input_road in intersection
    #       compare intersections
    #sort volumes
    #pick based on volume
    pass

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