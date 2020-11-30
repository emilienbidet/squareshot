import random
from src.wall import *
from src.game_config import *

class Map():

    def __init__(self, width=5, height=5, walls=50):
        self.width = width
        self.height = height
        self.cells = Maze(int(width/3+1), int(height/3+1))
        self.cells.makeMaze()
        print(self.cells)
        #self.cells.reduce(walls)
        print(self.cells)
        self.walls = pygame.sprite.Group()
        for x in range(width):
            self.walls.add(Wall(x,0))
            self.walls.add(Wall(x,height-1))
        for y in range(height):
            self.walls.add(Wall(0,y))
            self.walls.add(Wall(width-1,y))
        x, y = 0,0
        for c_x in range(1, width-2, 2):
            y = 0
            for c_y in range(1, height-2, 2):
                print(c_x,c_y)
                print(x,y)
                cell = self.cells.cellAt(x,y)
                if cell.walls['W']:
                    self.walls.add(Wall(c_x-1, c_y))
                if cell.walls['E']:
                    self.walls.add(Wall(c_x+1, c_y))
                if cell.walls['N']:
                    self.walls.add(Wall(c_x, c_y-1))
                if cell.walls['S']:
                    self.walls.add(Wall(c_x, c_y+1))
                y+= 1
            x += 1
        # for row in self.cells.maze_map:
        #     for cell in row:
        #         print(x,y)
        #         if cell.walls['W']:
        #             self.walls.add(Wall(x-1,y))
        #         if cell.walls['S']:
        #             self.walls.add(Wall(x,y-1))
        #         if cell.walls['E']:
        #             self.walls.add(Wall(x+1,y))
        #         if cell.walls['N']:
        #             self.walls.add(Wall(x,y+1))
        #         x +=3
        #     y +=3

    def draw(self,window):
        for wall in self.rect:
            wall.draw(window)

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

    def get_neighbourgs(self, cell):
        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cellAt(x2, y2)
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

    def get_walls_count(self):
        counter =0
        for x in range(self.nx):
            for y in range(self.ny):
                cell = self.cellAt(x, y)
                for wall in cell.walls:
                    if wall:
                        counter += 1
        return counter/2

    def reduce(self, walls=50):
        # Total number of cells to reduce
        wallsToRemove = self.get_walls_count() * walls / 100
        wallsRemoved = 0
        # Total number of cells.
        cell_stack = []
        current_cell = self.cellAt(0, 0)
        # Total number of visited cells during maze construction.

        while wallsRemoved < wallsToRemove:

            neighbours = self.get_neighbourgs(current_cell)

            if neighbours:
                direction, next_cell = random.choice(neighbours)
                current_cell.removeWall(next_cell, direction)
                wallsRemoved += 1

            # Choose a random neighbouring cell and move to it.

            current_cell = random.choice(random.choice(self.maze_map))
