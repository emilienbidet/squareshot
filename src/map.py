import random
from src.wall import *
from src.game_config import *

class Map():

    def __init__(self, width=5, height=5, walls=50):
        self.width = width
        self.height = height
        self.cells = Maze(width, height)
        print(self.cells)
        self.reduce(walls)
        print(self.cells)
        self.rect = []
        self.getHitbox()


    def draw(self,window):
        for wall in self.rect:
            wall.draw(window)

    def getHitbox(self):
        for y in range(self.height):
            for x in range(self.width):
                walls = self.cells.cellAt(x,y).walls
                if walls['N']:
                    self.rect.append(Wall(x, y-1))
                if walls['S']:
                    self.rect.append(Wall(x, y+1))
                if walls['E']:
                    self.rect.append(Wall(x+1, y))
                if walls['W']:
                    self.rect.append(Wall(x-1, y))

    def reduce(self, walls=50):
        # Total number of cells to reduce
        wallsToRemove = (self.height * self.width + 1 - self.height - self.width) * walls / 100
        wallsRemoved = 0
        while wallsRemoved < wallsToRemove:
            current_cell = random.choice(random.choice(self.cells.maze_map))
            neighbours = self.cells.findValidNeighbourg(current_cell)

            if neighbours:

                # Choose a random neighbouring cell and move to it.
                direction, next_cell = random.choice(neighbours)
                current_cell.removeWall(next_cell, direction)
                wallsRemoved += 1

class Cell:

    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def hasAllWalls(self):
        return all(self.walls.values())

    def removeWall(self, other, wall):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False

class Maze:
    def __init__(self, nx, ny):
        self.nx, self.ny = nx, ny
        self.maze_map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]

    def cellAt(self, x, y):
        return self.maze_map[x][y]

    def __str__(self):
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * self.nx * 2]
        for y in range(self.ny):
            maze_row = ['|']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def findValidNeighbourg(self, cell):
        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cellAt(x2, y2)
                if neighbour.hasAllWalls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def makeMaze(self):
        # Total number of cells.
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cellAt(0, 0)
        # Total number of visited cells during maze construction.
        nv = 1

        while nv < n:
            neighbours = self.findValidNeighbourg(current_cell)

            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.removeWall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1
map = Map(5,5,50)
