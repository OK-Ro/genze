import sys
from src.config_parser import parser_config
from src.maze.generator import MazeGenerator  # FIXED: Import the Class instead of the helper function
from src.render.ascii import AsciiRenderer


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 amaze_ing.py config.txt")
        sys.exit(1)

    try:
        # 1. Parse your configuration settings
        config = parser_config(sys.argv[1])
        
        # 2. Keep the generator instance alive in a variable
        generator = MazeGenerator(config)
        hex_grid = generator.generate()
        
        print("Maze generated successfully\n")
        
        # 3. Print the raw Hex matrix
        # print("--- Hexadecimal Output ---")
        # for row in hex_grid:
        #     print(" ".join(row))

        # 4. FIXED: Pass the active generator instance directly into your renderer!
        print("\n--- Visual ASCII Render ---")
        renderer = AsciiRenderer(generator)
        print(renderer.render())
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()