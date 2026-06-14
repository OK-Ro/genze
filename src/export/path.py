from src.maze.cell import N, E, S, W


def find_path(grid, start_position, end_position):
    # stack stores: (current position, path taken so far)
    search_stack = [(start_position, [start_position])]
    visited_cells = set()

    grid_height = len(grid)
    grid_width = len(grid[0])

    while search_stack:
        current_position, path_so_far = search_stack.pop()
        x, y = current_position

        if current_position == end_position:
            return path_so_far

        if current_position in visited_cells:
            continue

        visited_cells.add(current_position)

        current_cell = grid[y][x]

        # possible movements: (dx, dy, direction)
        possible_moves = [
            (0, -1, N),  # move north
            (1, 0, E),   # move east
            (0, 1, S),   # move south
            (-1, 0, W),  # move west
        ]

        for dx, dy, direction in possible_moves:
            next_x = x + dx
            next_y = y + dy
            next_position = (next_x, next_y)

            if 0 <= next_x < grid_width and 0 <= next_y < grid_height:
                if not current_cell.has_wall(direction):
                    new_path = path_so_far + [next_position]
                    search_stack.append((next_position, new_path))

    return []  # no path found


def convert_path_to_directions(path):
    directions = ""

    for index in range(1, len(path)):
        previous_x, previous_y = path[index - 1]
        current_x, current_y = path[index]

        if current_x > previous_x:
            directions += "E"
        elif current_x < previous_x:
            directions += "W"
        elif current_y > previous_y:
            directions += "S"
        else:
            directions += "N"

    return directions