def get_coordinate(record):
    new_turple = record[-1]
    return new_turple


def convert_coordinate(coordinate):
    coordinate = (coordinate[0], coordinate[1])

    return coordinate


def create_record(azara_record, rui_record):
    coordenate = azara_record[1]
    coordenate = convert_coordinate(coordenate)
    my_other_coordenate = rui_record[1]
    if coordenate == my_other_coordenate:
        return azara_record + rui_record
    elif coordenate != my_other_coordenate:
        return "not a match"
