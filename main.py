from format_data import load_file

def main():
    # Input processing
    input_lines = load_file('./datasets/a.txt').split("\n")[:-1]
    time, intersections, streets, cars, points = input_lines[0].split(" ")
    # List slice of streets from input
    street_info = input_lines[1:-int(cars)]
    create_int_dict(street_info)
    
        
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
    
if __name__ == '__main__':
    main()

