from format_data import load_file
import sys
from optimizer import *
def main(path):
    # Input processing
    input_lines = load_file(path).split("\n")[:-1]
    info = [int(val) for val in input_lines[0].split(" ")]
    time, intersections, streets, cars, points = info
    # List slice of streets from input
    street_info = input_lines[1:cars]
    intsec_dict = create_int_dict(street_info)
    #car_info = input_lines[intersections+cars:]
    #print(create_car_list(car_info))
    weightings = find_solution(time, intsec_dict, intersections, path, 20)


def create_int_dict(street_info):
    intersection_dict = {}
    for street in street_info:
        vals = street.split(" ")
        start = vals[0]
        end = vals[1]
        st_name = vals[2]
        if start not in intersection_dict:
            intersection_dict[start] = ([st_name] , [])
        else:
            intersection_dict[start][0].append(st_name)
        if end not in intersection_dict:
            intersection_dict[end] = ([], [st_name])
        else:
            intersection_dict[end][1].append(st_name)
    print(intersection_dict)
    return intersection_dict


def create_car_list(car_info):
    car_list = []
    for car in car_info:
        car_list.append(car.split(" ")[1:])
    return car_list

if __name__ == '__main__':
    assert (len(sys.argv) == 2)
    main(sys.argv[1])

