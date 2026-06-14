from src.export.path import find_path, convert_path_to_directions


def export_maze_hex(grid, entry, exit):
    output = ""

    # convert grid to hex
    for row in grid:
        output += "".join(cell.to_hex() for cell in row) + "\n"

    output += "\n"

    # entry + exit
    output += f"{entry[0]},{entry[1]}\n"
    output += f"{exit[0]},{exit[1]}\n"

    # compute path
    path = find_path(grid, entry, exit)
    output += convert_path_to_directions(path) + "\n"

    return output