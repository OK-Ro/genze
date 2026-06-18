from config_parser import parser_config
from src.maze.generator import MazeGenerator
from src.render.ascii import MazeRenderer
from src.maze.solver import MazeSolver
from src.maze.menu import MazeMenu
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <filename.txt>")
        sys.exit(1)

    filename = sys.argv[1]

    # =========================
    # STEP 1: CONFIG
    # =========================
    try:
        config = parser_config(filename)
        print("✔ Config loaded successfully")

    except FileNotFoundError as e:
        print(f"❌ File error: {e}")
        return

    except ValueError as e:
        print(f"❌ Config error: {e}")
        return

    # =========================
    # STEP 2: MENU SYSTEM
    # =========================
    try:
        menu = MazeMenu(config)
        menu.run()

    except Exception as e:
        print(f"❌ Menu error: {e}")
        return


if __name__ == "__main__":
    main()