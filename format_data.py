def load_file(path):
    f = open(path, 'r')
    contents = f.read()
    return contents


def write_to_file(path, data):
    # Clear file
    open(path, 'w').close()

    # Write to file
    f = open(path, 'a+')
    total_intersections = len(data)
    f.write(str(total_intersections))
    f.write('\n')
    for intersection in range(total_intersections):
        # write intersection number
        line1 = str(intersection)
        f.write(line1)
        f.write('\n')
        # write number of lights in sequence
        num_lights = str(len(data[intersection]))
        f.write(num_lights)
        f.write('\n')
        for sequence in data[intersection]:
            l = sequence[0] + " " + str(sequence[1])
            f.write(l)
            f.write('\n')

    f.close()
