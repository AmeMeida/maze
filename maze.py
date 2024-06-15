from dataclasses import dataclass
from os import path

@dataclass
class Tile:
    empty: bool

    def __str__(self) -> str:
        return " " if self.empty else "#"

@dataclass
class Wall(Tile):
    down_exposed: bool

    def __post_init__(self):
        self.empty = False

    def __str__(self) -> str:
        if self.empty:
            return " "
        if self.down_exposed:
            return "%"
        else:
            return "#"

mazes: list[list[Tile | None]] = []

for i in range(1, 16):
    filepath = f"mazes/maze{i}.txt"

    if not path.isfile(filepath):
        break
    
    maze = open(filepath)

    for i, line in enumerate(maze):
        line = line.strip()
        mazes.append([])

        for j, cell in enumerate(line):
            if cell == " ":
                mazes[i].append(Tile(True))
            else:
                mazes[i].append(Wall(False, True))
                if isinstance(mazes[i-1][j], Wall):
                    mazes[i-1][j].down_exposed = False

for line in mazes:
    print(*line, sep="")
