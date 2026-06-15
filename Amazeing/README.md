Amazeing/
├── .gitignore
├── Makefile
├── README.md
├── config.txt                   # Your default configuration file
├── amaze_ing.py                 # Main executable script (Mandatory name!)
│
├── src/                         # All core application logic
│   ├── __init__.py
│   ├── config_parser.py         # Parses config.txt handles type conversions
│   ├── ui/                      # Visual representations (ASCII / MLX)
│   │   ├── __init__.py
│   │   └── renderer.py          # Handles rendering, color swaps, shortest path
│   │
│   └── maze/                    # This directory will be your standalone package!
│       ├── __init__.py
│       ├── generator.py         # Contains the MazeGenerator class
│       └── utils.py             # Math, 42-pattern stamps, or coordinate checks
│
├── pyproject.toml               # Modern build configuration for packaging mazegen
└── setup.py                     # (Optional) Alternative or legacy packaging file



🧱 Breaking Down the Key Components
1. The Main Executable (amaze_ing.py)
This file lives at the absolute root of your project because the grading environment/peers expect to run exactly: python3 amaze_ing.py config.txt. It should act purely as an entry point:

Parses arguments (sys.argv).

Calls src.config_parser.

Initializes the MazeGenerator.

Feeds the maze data into your visual renderer (src.ui.renderer).

Writes the resulting hexadecimal bits to your output file.

2. The Reusable Module (src/maze/)
Chapter VI states that your generation logic must be completely standalone. By putting all maze algorithms and cell structures inside src/maze/, you keep it isolated from your terminal rendering or UI code.

When you build your pip package, you will configure your build tool to bundle only this directory.

3. The pyproject.toml (Crucial for the Evaluation)
During your defense, the grading sheet or your peers will ask you to build your package from scratch in a virtual environment. To handle this cleanly, place a pyproject.toml file at your root: