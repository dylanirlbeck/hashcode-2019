def get_vh(file_name):
    """Returns vertical, horizontal lists of [id, [tags]]"""
    file = open(file_name, "r")

    lines = file.read().split("\n")

    horizontal = []

    vertical = []

    id = 0
    
    print(lines[1:])

    for line in lines[1:-1]:
        new_element = []
        if line[0] == "H":
            new_element.append(id)
            new_element.append(line.split()[2:])
            horizontal.append(new_element)
        else:
            new_element.append(id)
            new_element.append(line.split()[2:])
            vertical.append(new_element)
        id += 1



