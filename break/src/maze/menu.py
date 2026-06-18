from src.maze.generator import MazeGenerator
from src.render.ascii import MazeRenderer
from src.maze.solver import MazeSolver


class MazeMenu:
    def __init__(self, config):
        self.config = config

        self.maze = MazeGenerator(config)
        self.maze.generate()

        self.renderer = MazeRenderer(self.maze)
        self.solver = MazeSolver(
            self.maze.grid,
            self.maze.entry,
            self.maze.exit
        )

        self.path = self.solver.solve()
        self.show_path = True
        self.colors = ["blue", "green", "red"]
        self.color_index = 0

    def run(self):
        while True:
            print("\n=== A-MAZE-ING MENU ===")
            print("1. Generate new maze")
            print("2. Show/Hide path")
            print("3. Rotate colors")
            print("4. Quit")

            choice = input("Choose 1-4: ")

            # -------------------------
            # 1. NEW MAZE
            # -------------------------
            if choice == "1":
                self.maze = MazeGenerator(self.config)
                self.maze.generate()

                self.solver = MazeSolver(
                    self.maze.grid,
                    self.maze.entry,
                    self.maze.exit
                )
                self.path = self.solver.solve()

            # -------------------------
            # 2. TOGGLE PATH
            # -------------------------
            elif choice == "2":
                self.show_path = not self.show_path

            # -------------------------
            # 3. COLOR ROTATION
            # -------------------------
            elif choice == "3":
                self.color_index = (self.color_index + 1) % len(self.colors)
                self.renderer = MazeRenderer(self.maze)

            # -------------------------
            # 4. EXIT
            # -------------------------
            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option")
                continue

            # -------------------------
            # RENDER
            # -------------------------
            if self.show_path:
                print(self.renderer.block_render(self.path))
            else:
                print(self.renderer.block_render(None))