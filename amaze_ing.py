import sys
from src.config_parser import parser_config
from src.maze.generator import MazeGenerator
from src.render.ascii import render_maze
from src.export.hex import export_maze_hex


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    try:

        config = parser_config(sys.argv[1])

        maze = MazeGenerator(config)
        grid = maze.generate()

        print("Maze generated successfully")
        print("Size:", config["WIDTH"], "x", config["HEIGHT"])
        print("Entry:", config["ENTRY"], "Exit:", config["EXIT"])
        # print("Grid preview:", grid[0])
        # print(render_maze(grid))
        print(render_maze(grid, config["ENTRY"], config["EXIT"]))


        content = export_maze_hex(
            grid,
            config["ENTRY"],
            config["EXIT"]
        )
        with open(config["OUTPUT_FILE"], "w") as f:
            f.write(content)

        print(f"Output file created: {config['OUTPUT_FILE']}")

    except Exception as e:
        print("Error:", e)
        sys.exit(1)